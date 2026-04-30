#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# Local caching to save API units (SerpAPI limit: 100/month)
# Sheety API is excluded from cache to ensure we always get fresh spreadsheet data
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600, # Cache other requests for 1 hour
    }
)


def main():
    # Creating instances of my classes
    # DataManager to manage spreadsheet data
    data_manager = DataManager()
    # FlightSearch to perform the actual flight queries
    flight_search = FlightSearch()
    # NotificationManager to send alerts
    notification_manager = NotificationManager()

    # Retrieve all data from the Google Sheet
    sheet_data = data_manager.get_destination_data()

    # Set the starting point for the search
    tomorrow = datetime.now() + timedelta(days=1)
    # Set the search limit -> the date 6 months from today
    till_date = datetime.now() + timedelta(days=180)
    # The starting airport IATA code (Ljubljana, Slovenia)
    ORIGIN_CITY_IATA = "LJU"

    print(f"--- Starting flight search from {ORIGIN_CITY_IATA} ---")

    # Iterate through each destination entry retrieved from the spreadsheet
    for destination in sheet_data:
        print(f"Checking flights for {destination['city']}...")

        # Call the API to search for flights based on origin, destination, and dates
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,       # Starting point
            destination["iataCode"],# Destination from the current sheet row
            from_time=tomorrow,     # Earliest departure date
            to_time=till_date       # Latest departure date
        )

        # Check if the API returned no results to prevent errors in the next step
        if not flights:
            print(f"No flights found for {destination['city']}.")
            # Skip the rest of the loop for this destination and move to the next one
            continue

        # among all flights from the search results, extract the cheapest one
        cheapest_flight = find_cheapest_flight(
            data=flights,  # The list of flights returned by the API
            return_date=till_date.strftime("%Y-%m-%d")  # Format the date for the function
        )

        # Skip this destination if the flight data is missing or price is not available
        if cheapest_flight is None or cheapest_flight.price == "N/A":
            # Move to the next destination in the loop
            continue
        print(f"Current lowest for {destination['city']}: {cheapest_flight.price} EUR")

        # if found price is lower as one stored in the spreadsheet
        if cheapest_flight.price < destination["lowestPrice"]:
            print(f"!!! Price Drop Alert for {destination['city']} !!!")

            # Update the specific row in Google Sheets with the new record price
            data_manager.update_lowest_price(destination["id"], cheapest_flight.price)

            # Construct and send an SMS alert with all relevant flight details
            notification_manager.send_sms(
                message_body=(
                    f"Low price alert! Only {cheapest_flight.price} EUR to fly "
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
                )
            )


# Check if the script is being run directly and not imported
if __name__ == "__main__":
    # Execute the main function to start the program
    main()

