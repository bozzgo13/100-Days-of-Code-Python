import os
from datetime import datetime
import requests
from dotenv import load_dotenv

# nutrition api docs Link: https://app.100daysofpython.dev/services/nutrition/docs
# Sheety api docs Link: https://sheety.co/docs

load_dotenv()

# List of required environment variables
required_vars = ['API_KEY','APP_ID','WEIGHT_KG', 'HEIGHT_CM', 'AGE', 'GENDER', 'SHEETY_ENDPOINT', 'SHEETY_USERNAME', 'SHEETY_PASSWORD']

# Check if any variable is missing from the .env file
for var in required_vars:
    if os.getenv(var) is None:
        raise ValueError(f"Missing environment variable: {var}")

API_KEY = os.getenv('API_KEY')
APP_ID = os.getenv('APP_ID')
try:
    # Convert strings to appropriate numeric types
    WEIGHT_KG = float(os.getenv('WEIGHT_KG'))
    HEIGHT_CM = float(os.getenv('HEIGHT_CM'))
    AGE = float(os.getenv('AGE'))
except ValueError as e:
    # Failed type conversions
    print(f"Configuration error: {e}")
GENDER = os.getenv('GENDER')

# Sheety params
GOOGLE_SHEET_NAME = 'Workot'
# URL Structure: https://api.sheety.co/username/projectName/sheetName
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]


def save_into_sheet(endpoint, sheet_name, result, username, password):
    # Get current date and current time
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    # extrude data from result
    inputs = None
    for exercise in result["exercises"]:
        inputs = {
            sheet_name: {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

    response = requests.post(url=endpoint,json=inputs,auth=(username,password)) # Sheety Basic Auth Authentication
    return response

api_url = 'https://app.100daysofpython.dev'
nutrition_endpoint = '/v1/nutrition/natural/exercise'
# Calculate calories burned from a natural language exercise description.
# POST /v1/nutrition/natural/exercise
# body
# {
#   "query": "ran 3 miles",
#   "weight_kg": 70,                  // Optional: Weight in kg (1-500)
#   "height_cm": 175,                 // Optional: Height in cm (1-300)
#   "age": 30,                        // Optional: Age (1-150)
#   "gender": "male"                  // Optional: "male" or "female"
# }


nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query =input("What did you do today? Type EXIT to close the program\n")
while query. lower() != "exit":
    nutrition_params = {
        "query": query,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
        "gender": GENDER
    }

    print(f"Request URL: {api_url+nutrition_endpoint}")
    #print(f"Request Header: {nutrition_headers}")
    print(f"Request Body:{nutrition_params}")

    nutrition_response = requests.post(url=api_url+nutrition_endpoint, json=nutrition_params, headers=nutrition_headers)
    print(f"Response Body:{nutrition_response.text}")
    # example of nutrition_response.text
    # {
    #   "exercises":[
    #   {
    #     "tag_id":50,
    #     "user_input":"ran 5km",
    #     "duration_min":30,
    #     "met":9.31,
    #     "nf_calories":440,
    #     "photo":
    #     {
    #       "highres":"https://placeholder.not-a-real-url.com/exercise/50_highres.jpg",
    #       "thumb":"https://placeholder.not-a-real-url.com/exercise/50_thumb.jpg",
    #       "is_user_uploaded":false
    #     },
    #     "compendium_code":12050,
    #     "name":"running",
    #     "description":null,
    #     "benefits":null
    #   }
    # ]}

    sheety_response = save_into_sheet(SHEETY_ENDPOINT, GOOGLE_SHEET_NAME, nutrition_response.text, SHEETY_USERNAME, SHEETY_PASSWORD)
    # Example of response
    # {
    #   'workouts':
    #   [{
    # 	  'date': '30/04/2026',
    # 	  'time': '15:54:22',
    # 	  'exercise': 'Running',
    # 	  'duration': 35,
    # 	  'calories': 207,
    # 	  'id': 2
    # 	}]
    # }
    print(f"Sheety Response: \n {sheety_response.text}")

    query=input("What did you do today? Type EXIT to close the program\n")
