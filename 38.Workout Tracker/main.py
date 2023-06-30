from datetime import datetime
import os
import requests

APP_ID = os.environ["YOUR_APP_ID"]
API_KEY = os.environ["YOUR_API_KEY"]
GENDER = "male"
WEIGHT = 83
HEIGHT = 173
AGE = 20
TOKEN = os.environ["TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = os.environ["YOUR_SHEET_ENDPOINT"]


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


parameters = {
    "query": input("Tell me which exercises you did : "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
# print(result)
time = datetime.now().strftime("%X")
dt = datetime.now().strftime("%d/%m/%Y")
# print(duration)
for exc in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": dt,
            "time": time,
            "exercise": exc["name"].title(),
            "duration": exc["duration_min"],
            "calories": exc["nf_calories"]
        }
    }

    #No Auth
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    # sheet_response.raise_for_status()

    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)