# weathrt forecast

import requests
from twilio.rest import Client
# Opneweather API key
# Get your real API key at https://home.openweathermap.org/api_keys
API_KEY = "insert_magic_here"
LATITUDE = 46.394569
LONGITUDE = 15.660400

parameters = {
    "lat": LATITUDE,
    "lon":LONGITUDE,
    "appid":API_KEY,
    "cnt":4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
#print(response.url)
response.raise_for_status()
#print(f"Status code: {response.status_code}")
response_Json = response.json()
list =response_Json['list']
will_rain= False
for moment in list:
    weather=moment['weather'][0]
    #print(weather)

    if weather['main'] == "Rain":
        will_rain = True
        break



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
#print(response_Json)

# Sending message via SMS
if will_rain:
    # Credentials from the Twilio Console
    account_sid = 'ACCOUNT_SID'
    auth_token = 'AUTH_TOKEN'
    twilio_number = '+1234567890'  # Your Twilio phone number
    receiver_number = '+38640707070'

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Send the SMS message
    message = client.messages.create(
        from_=twilio_number,
        body="Tako your umbrella with you!",
        to=receiver_number
    )    
    print(f"Message sent successfully! SID: {message.sid}")



