import requests
import datetime as dt 
from datetime import datetime, timedelta
import json
import csv

API_KEY = open('weather_api_key', 'r').read()
LOCATION = "Rotterdam" 

date = "2025-04-13" 
url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={LOCATION}&dt={date}"

response = requests.get(url)
data = response.json()



csv_filename = "BNP-Paribas-Open-weather-hourly.csv"