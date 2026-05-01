import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# Using cache to avoid hitting API rate limits during testing.
# Sheety is excluded from cache to ensure we always read/write fresh price data.
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": 0,
        "*": 3600
    }
)

# Constants & Setup
ORIGIN_CITY_IATA = "LJU"  # IATA for Ljubljana
SEARCH_WINDOW_MONTHS = 6

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


def manage_flight_search():
    # Fetch destination and customer data from the spreadsheet
    sheet_data = data_manager.get_destination_data()
    customer_data = data_manager.get_customer_emails()
    customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]

    # Define search timeframe
    tomorrow = datetime.now() + timedelta(days=1)
    six_months_later = datetime.now() + timedelta(days=(SEARCH_WINDOW_MONTHS * 30))

    for destination in sheet_data:
        dest_code = destination["iataCode"]
        print(f"--- Searching for {destination['city']} ({dest_code}) ---")

        # 1. Attempt: Search for direct flights
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            dest_code,
            from_time=tomorrow,
            to_time=six_months_later
        )
        cheapest_flight = find_cheapest_flight(flights, return_date=six_months_later.strftime("%Y-%m-%d"))

        # 2. Attempt: Search for indirect flights if no direct options are found
        if cheapest_flight.price == "N/A":
            print(f"No direct flights to {dest_code}. Searching for indirect options...")
            stopover_flights = flight_search.check_flights(
                ORIGIN_CITY_IATA,
                dest_code,
                from_time=tomorrow,
                to_time=six_months_later,
                is_direct=False
            )
            cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_months_later.strftime("%Y-%m-%d"))

        # Notification Logic
        # Check if a flight was found and if it's cheaper than the price currently in the sheet
        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            process_alerts(destination, cheapest_flight, customer_email_list)


def process_alerts(destination, flight, email_list):
    """Handles price updates and notification dispatch."""

    # Format the notification message based on connection type
    connection_type = "direct" if flight.stops == 0 else f"{flight.stops} stop(s)"

    message = (
        f"Low price alert! Only {flight.price} EUR to fly from "
        f"{flight.origin_airport} to {flight.destination_airport} ({connection_type}).\n"
        f"Departure: {flight.out_date} | Return: {flight.return_date}"
    )

    print(f"Deal found for {destination['city']}! Updating database and sending alerts...")

    # Update the lowest price in Google Sheets
    data_manager.update_lowest_price(destination["id"], flight.price)

    # Dispatch notifications via WhatsApp and Email
    notification_manager.send_whatsapp(message_body=message)
    notification_manager.send_emails(email_list=email_list, email_body=message)


if __name__ == "__main__":
    manage_flight_search()