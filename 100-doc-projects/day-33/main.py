import requests
import json
from datetime import datetime

MY_LAT = 13.056865
MY_LoNG = 77.623528

parameters = {
    "lat": MY_LAT,
    "lng": MY_LoNG,
    "formatted": 0  # Set to 0 to get the time in UTC format
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # Check if the request was successful
data = response.json()  # Convert the response to JSON format
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
time_now = datetime.now()
print(sunset)