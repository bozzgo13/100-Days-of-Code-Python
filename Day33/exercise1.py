# Get current ISS (International Space Station) position
import requests

# API Docs http://open-notify.org/Open-Notify-API/ISS-Location-Now/
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
iss_position =(latitude, longitude)
print(f"ISS current position: {iss_position}")
# To se where this position is, you can use latlong page
print(f"You can check it out on LatLong.net: https://www.latlong.net/c/?lat={latitude}&long={longitude}")
print(f"Google maps link: https://www.google.com/maps/search/?api=1&query={latitude},{longitude}")


# Example of response
# ISS current position: (40.897, -93.5706)
# You can check it out on LatLong.net: https://www.latlong.net/c/?lat=40.897&long=-93.5706
# Google Maps link: https://www.google.com/maps/search/?api=1&query=40.897,-93.5706


