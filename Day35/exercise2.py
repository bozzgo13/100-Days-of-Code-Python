# weathrt forecast

import requests

# Opneweather API key
# Get your real API key at https://home.openweathermap.org/api_keys
API_KEY = "insert_magic_here"
LATITUDE = 46.394569
LONGITUDE = 15.660400

parameters = {
    "lat": LATITUDE,
    "lon":LONGITUDE,
    "appid":API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(f"Status code: {response.status_code}")
response_Json = response.json()
# part of response:
# {
#   "cod": "200",
#   "message": 0,
#   "cnt": 40,
#   "list": [
#     {
#       "dt": 1774569600,
#       "main": {
#         "temp": 278,
#         "feels_like": 272.39,
#         "temp_min": 278,
#         "temp_max": 279.32,
#         "pressure": 1004,
#         "sea_level": 1004,
#         "grnd_level": 956,
#         "humidity": 76,
#         "temp_kf": -1.32
#       },
#       "weather": [
#         {
#           "id": 500,
#           "main": "Rain",
#           "description": "light rain",
#           "icon": "10n"
#         }
#       ],
#       "clouds": {
#         "all": 100
#       },
#       "wind": {
#         "speed": 10.59,
#         "deg": 6,
#         "gust": 23.95
#       },
#       "visibility": 6971,
#       "pop": 1,
#       "rain": {
#         "3h": 1.82
#       },
#       "sys": {
#         "pod": "n"
#       },
#       "dt_txt": "2026-03-27 00:00:00"
#     },
#	  ...
#   ],
#   "city": {
#     "id": 3192603,
#     "name": "Pragersko",
#     "coord": {
#       "lat": 46.3946,
#       "lon": 15.6604
#     },
#     "country": "SI",
#     "population": 1098,
#     "timezone": 3600,
#     "sunrise": 1774500547,
#     "sunset": 1774545414
#   }
# }
print(response_Json)
