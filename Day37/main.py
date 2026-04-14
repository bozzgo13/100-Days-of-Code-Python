import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv() # Load variables from the .env file into the system environment


USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')
GRAPH_ID = "test1"
# Pixela docs: https://docs.pixe.la/


# 1. create user
users_endpoint = "https://pixe.la/v1/users"
user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}

#response = requests.post(users_endpoint, json=user_params)
#print(response.text)

# 2. create graph
graph_endpoint = (f"https://pixe.la/v1/users/{USERNAME}/graphs")
graph_params = {
    "id":GRAPH_ID,
    "name":"Test 100 days of code",
    "unit": "commit",
    "type": "int",
    "color": "momiji"
}
grahp_heaaders={
    "X-USER-TOKEN": TOKEN
}

#new_graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=grahp_heaaders)
#print(new_graph_response.text)

# 3. add quantity to specific date on graph
quantity_endpoint = (f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}")

today = datetime.now()
# format as string yyyymmdd
formatted_date = today.strftime("%Y%m%d")

quantity_params = {
    "date":formatted_date,
    "quantity":"10"
}
quantity_heaaders={
    "X-USER-TOKEN": TOKEN
}

#quantity_graph_response = requests.post(url=quantity_endpoint, json=quantity_params, headers=quantity_heaaders)
#print(quantity_graph_response.text)


quantity_params["date"] = "20260413"
quantity_graph_response = requests.post(url=quantity_endpoint, json=quantity_params, headers=quantity_heaaders)

# 4. update already existing pixel
update_endpoint = (f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20260414")
update_body = {
    "quantity":"25"
}
update_heaaders={
    "X-USER-TOKEN": TOKEN
}

#print(update_endpoint)
#update_graph_response = requests.put(update_endpoint, json=update_body, headers=update_heaaders)
#print(update_graph_response.text)


# 5. delete existing pixel
delete_endpoint = (f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20260414")

delete_heaaders={
    "X-USER-TOKEN": TOKEN
}

print(delete_endpoint)
delete_graph_response = requests.delete(delete_endpoint,  headers=delete_heaaders)
print(delete_graph_response.text)
