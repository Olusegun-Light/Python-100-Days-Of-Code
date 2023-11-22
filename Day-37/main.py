import requests
from datetime import datetime

USERNAME = "your_name"
TOKEN = "your_password"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 1) Create user account
response = requests.post(url=pixela_endpoint, json=user_data)
print(response.text)

# 2) Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {"X-USER-TOKEN": TOKEN}
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)
# Make a request to your browser to get your graph "https://pixe.la/v1/users/<username>/graphs/<graphid>.html"

# 3) Add pixel to the tracker
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)

# 4) Update pixel
date = today.strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"
pixel_update_data = {"quantity": "5"}

pixel_update_response = requests.put(
    url=pixel_update_endpoint, json=pixel_update_data, headers=headers
)
print(pixel_update_response)

# 5) Delete pixel

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"
pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(pixel_delete_response.text)
