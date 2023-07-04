import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/9f1ef6678575af9dd08f244a8918a0a4/flightDeals/prices"
class DataManager:
    def __init__(self):
    #This class is responsible for talking to the Google Sheet.
        self.auth_header =   {
            "Authorization": f"Bearer udankhatoladeals"
         }
        self.flight_data={}

    def info(self):
        response = requests.get(sheety_endpoint, headers=self.auth_header)
        response.raise_for_status()
        self.flight_data = response.json()["prices"]
        return self.flight_data

    def update_info(self):
        for cities in self.flight_data:
            new_data = {
                "price": {
                    "iataCode": cities["iataCode"]
                }
            }
            # pprint(cities)
            update_endpoint = f"{sheety_endpoint}/{cities['id']}"
            update = requests.put(update_endpoint, json=new_data, headers=self.auth_header)
            return update
            # print(update.text)