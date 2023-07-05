import requests
import os
from pprint import pprint

sheety_endpoint = os.environ.get("SHEET_ENDPOINT")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")


class DataManager:
    def __init__(self):
        # This class is responsible for talking to the Google Sheet.
        self.auth_header = {
            "Authorization": f"Bearer {AUTH_TOKEN}"
        }
        self.flight_data = {}

    def info(self):
        response = requests.get(sheety_endpoint, headers=self.auth_header)
        response.raise_for_status()
        self.flight_data = response.json()["prices"]
        return self.flight_data

    def update_info(self):
        for cities in self.flight_data:
            new_data = {
                "price": {
                    "iataCode": cities["iataCode"],
                    "lowestPrice": cities["price"]
                }
            }
            # pprint(cities)
            update_endpoint = f"{sheety_endpoint}/{cities['id']}"
            update = requests.put(update_endpoint, json=new_data, headers=self.auth_header)
            return update
            # print(update.text)

    def get_customer_emails(self):
        customers_endpoint = "SHEETY_USERS_ENDPOINT"  # SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
