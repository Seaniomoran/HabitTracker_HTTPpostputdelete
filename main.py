import os

import requests
from datetime import datetime

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_ACCOUNT = os.getenv("PIXELA_ACCOUNT")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_ACCOUNT,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  #commented out because user profile was successfully created

graph_endpoint = f"{pixela_endpoint}/{PIXELA_ACCOUNT}/graphs"
graph_id = "graph1"

# graph_config = {
#     "id": graph_id,
#     "name": "Reading Graph",
#     "unit": "hour",
#     "type": "float",
#     "color": "ajisai",
# }

headers = {
    "X-User-Token": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint,  json=graph_config, headers=headers)
# print(response.text)  #comment out because graph created successfully

#add new pixel/ comment out lines 50->end/ change line 39
formatted_date = datetime.now().strftime("%Y%m%d")
hours: float = 5

graph_config = {
    "date": formatted_date,
    "quantity": f"{hours}"
}

graph_endpoint = f"{graph_endpoint}/{graph_id}"
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# correcting a data-pixel/ comment out lines 37-50 and 61->end/ edit lines 51 & 52
date_of_correction = datetime(year=2022, month=6, day=13).strftime("%Y%m%d")
hours: float = 5.4
graph_config["quantity"] = f"{hours}"

del graph_config["date"]

update_endpoint = f"{graph_endpoint}/{graph_id}/{date_of_correction}"
response = requests.put(url=update_endpoint, json=graph_config, headers=headers)
print(response.text)

# delete a data-pixel/ comment out lines 37->65/ edit line 66
date_of_correction = datetime(year=2022, month=6, day=13).strftime("%Y%m%d")
delete_endpoint = f"{graph_endpoint}/{graph_id}/{date_of_correction}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
