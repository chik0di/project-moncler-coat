# Change the LOCATION variable to the place you want to collect real-time weather data

import requests

API_KEY = open('weather_api_key', 'r').read()
LOCATION = "New York" 

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}"

response = requests.get(url)
data = response.json()

print(data)