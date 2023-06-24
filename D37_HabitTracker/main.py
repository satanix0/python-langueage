'''
Please Visit the pixela documentation for more information about the pixel graph.
LINK:- https://docs.pixe.la/

To see the graph visit 
https://pixe.la/v1/users/satan/graphs/graph1.html

refresh the page after each change to see the changes.

requests.get() : used to retrieve data from APIs
requests.post() : used to send our data to APIs
requests.delete() : used to delete our data from APIs
requests.put() : used to update our data in APIs

'''


import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER = "satan"
TOKEN = "kjkjdbsvkjsdb"
GRAPH_ID = "graph1"

# Creating a User
user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response=requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Creating a Graph for Tracking a habit
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Tracking",
    "Unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response=requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Creating Pixels on the graph
PXL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1"
PXL_HEAD = {
    "X-USER-TOKEN": TOKEN,
}

# strftime is not used here to covert the date in the specified format
today = datetime.now()
today_str = today.strftime("%Y%m%d")

PXL_PARAM = {
    "date": "20220729",
    "quantity": "10",
}

# response = requests.post(url=PXL_ENDPOINT, json=PXL_PARAM, headers=PXL_HEAD)
# print(response.text)

# Updating a pixel on the graph
PXL_UPDT_EP = f"{PXL_ENDPOINT}/{today_str}"

PXL_UPDT_PARAM = {
    "quantity": "13"
}

# deleting a pixel on the graph.
PXL_DLT_EP = f"{PXL_ENDPOINT}/20220731"
response = requests.delete(url=PXL_DLT_EP, headers=PXL_HEAD)
print(response.text)
