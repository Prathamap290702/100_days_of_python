import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "zorrroo"
TOKEN = "roronoazoro+--"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = str(datetime.now().strftime("%Y%m%d"))
pixel_endpoint =  f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": today,
    "quantity": input("How much time did you read today?"),
}
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{today}"
new_pixel_data = {
    "quantity": input("What is the value you wamt to update?")
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = update_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)