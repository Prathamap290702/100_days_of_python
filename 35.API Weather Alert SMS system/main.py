import requests
import os
from twilio.rest import Client


account_sid = "AC21310aa422dbd4a715b68feb6416b35e"
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

api_key = os.environ.get("WA_API_KEY")
Weather_api_endpoint = "https://api.weatherapi.com/v1/forecast.json"
weather_params = {
    "key": api_key,
    "q": "Kalyan",
    "days":1,
    "aqi":"no",
    "alerts":"no"
}
response = requests.get(Weather_api_endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["forecast"]["forecastday"][0]["hour"][:12]
# print(weather_slice)
will_rain = False
for hour_data in weather_slice:
    # print(hour_data["will_it_rain"])
    rain_condn = bool(hour_data["will_it_rain"])
    if rain_condn:
        will_rain = True
if will_rain:
    # print("Bring Umbrella")
    message = client.messages \
        .create(
        from_='+14175243043',
        body='Its going to rain today, Dont forget to take an ☔',
        to=os.environ.get("NUM")
    )
    print(message.status)
# print(weather_data["forecast"]["forecastday"][0]["hour"])