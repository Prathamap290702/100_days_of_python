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
sheet_data = sheet.update_info()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = flight_search.get_price(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:

        users = sheet.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, message)