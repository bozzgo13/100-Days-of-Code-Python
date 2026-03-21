# Get sunset and sunrise times
import requests

# API Docs https://sunrise-sunset.org/api/
location_MB = (46.554649, 15.645881)
location_LJ = (46.056946, 14.505752)
date = "today"
url = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": location_MB[0],
    "lng": location_MB[1],
    "date": date
}
# Alternatively, we can construct the full URL with query parameters manually:
# url = f"https://api.sunrise-sunset.org/json?lat={location_MB[0]}&lng={location_MB[1]}&date={date}"
response = requests.get(url=url, params=parameters)

# example of API response (formated):
# {
#   "results": {
#     "sunrise": "4:56:45 AM",
#     "sunset": "5:12:24 PM",
#     "solar_noon": "11:04:35 AM",
#     "day_length": "12:15:39",
#     "civil_twilight_begin": "4:28:10 AM",
#     "civil_twilight_end": "5:40:59 PM",
#     "nautical_twilight_begin": "3:52:42 AM",
#     "nautical_twilight_end": "6:16:28 PM",
#     "astronomical_twilight_begin": "3:16:10 AM",
#     "astronomical_twilight_end": "6:52:59 PM"
#   },
#   "status": "OK",
#   "tzid": "UTC"
# }


response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"Sunrise for {date}: {sunrise}")
print(f"Sunset for {date}: {sunset}")

# example of output
# request: https://api.sunrise-sunset.org/json?lat=46.554649&lng=15.645881&date=today
# Sunrise for today: 4:56:45 AM
# Sunset for today: 5:12:24 PM
