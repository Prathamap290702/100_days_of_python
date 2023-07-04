#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from pprint import pprint
from notification_manager import NotificationManager
from flight_search import FlightSearch


sheet = DataManager()
flight_search = FlightSearch()
sheet_info = sheet.info()
ORIGIN_CITY_IATA = "BOM"
notification_manager = NotificationManager()
# pprint(sheet_info)


if sheet_info[0]["iataCode"] == "":
    for cities in sheet_info:
        cities["iataCode"] = flight_search.get_destination(cities["city"])
        # flight_search.get_destination(cities["city"])
        # pprint(sheet_info)
    sheet.flight_data = sheet_info
sheet.update_info()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# print(tomorrow.strftime("%d/%m/%Y"))
for destination in sheet_info:
    flight = flight_search.get_price(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )