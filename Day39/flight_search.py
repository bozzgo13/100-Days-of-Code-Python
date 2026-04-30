import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """
    def __init__(self):
        self._api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Check for flights between origin_city_code and destination_city_code from from_time to to_time
        :param origin_city_code: IATA code (3-character airport identifier) of origin
        :param destination_city_code: IATA code (3-character airport identifier) of destination
        :param from_time: Search for flights from this date
        :param to_time: Search for flights until this date
        :return:
        """
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "EUR",
            "api_key": self._api_key,
        }

        response = requests.get(url=SERPAPI_ENDPOINT, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data
