# current weathrt

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

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
response_Json = response.json()
# example of response
# {
# 'coord':
# {
#   'lon': 15.6604,
#   'lat': 46.3946},
#   'weather':
#   [
#       {
#           'id': 520,
#           'main': 'Rain',
#           'description': 'light intensity shower rain',
#           'icon': '09n'
#       }
#   ],
#   'base': 'stations',
#   'main':
#   {
#       'temp': 277.23,
#       'feels_like': 270.59,
#       'temp_min': 276.56,
#       'temp_max': 277.72,
#       'pressure': 1004,
#       'humidity': 80,
#       'sea_level': 1004,
#       'grnd_level': 958
#   },
#   'visibility': 10000,
#   'wind':
#   {
#       'speed': 13.89,
#       'deg': 350,
#       'gust': 19.55
#   },
#   'rain':
#   {
#       '1h': 1.69
#   },
#   'clouds':
#   {
#       'all': 100
#   },
#   'dt': 1774560342,
#   'sys':
#   {
#       'type': 1,
#       'id': 6825,
#       'country': 'SI',
#       'sunrise': 1774500547,
#       'sunset': 1774545414
#   },
#   'timezone': 3600,
#   'id': 3192603,
#   'name': 'Pragersko',
#   'cod': 200
# }
print(response_Json)
