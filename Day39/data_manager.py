import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        """
        Get all lowest prices stored in Google Sheets
        :return:
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_lowest_price(self, row_id, new_price):
        """
        Update lower price than what is stored in Google Sheets for specific destination under row: row_id
        :param row_id: Row ID for Sheety to know which row we want to update
        :param new_price: New lowest price
        :return:
        """
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self._authorization
        )
