# Adjust START_DATE & END_DATE to the date-range you wish to extract hourly weather forecasts

# Adjust LOCATION to the case study

# Limit your date to a range of 14 days

import requests
import datetime as dt 
from meteostat import Hourly, Daily
from datetime import datetime
from datetime import datetime, timedelta
import json
import csv

API_KEY = open('weather_api_key', 'r').read().strip()
LOCATION = "Tokyo"
START_DATE = datetime(2025, 3, 1)
END_DATE = datetime(2025, 12, 31)

all_forecasts = []

current_date = START_DATE
while current_date <= END_DATE:
    date_str = current_date.strftime('%Y-%m-%d')
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={LOCATION}&dt={date_str}&days=1"

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print(f"Error fetching data for {date_str}: {data['error']['message']}")
        break 

    forecast_day = data.get("forecast", {}).get("forecastday", [])[0]  # Extract forecast for the day

    if forecast_day:
        for hour_data in forecast_day.get("hour", []): 
            all_forecasts.append({
                "date": forecast_day["date"],
                "time": hour_data["time"],
                
                "temp_c": hour_data["temp_c"],
                "temp_f": hour_data["temp_f"],
                "condition": hour_data["condition"]["text"], 
                "wind_mph": hour_data["wind_mph"],
                "wind_kph": hour_data["wind_kph"],
                "wind_degree": hour_data["wind_degree"],
                "wind_direction": hour_data["wind_dir"],

                "pressure_mb": hour_data["pressure_mb"],
                "pressure_in": hour_data["pressure_in"],
                "precip_mm": hour_data["precip_mm"],
                "precip_in": hour_data["precip_in"],

                "snow_cm": hour_data["snow_cm"],
                "humidity": hour_data["humidity"],
                
                "cloud": hour_data["cloud"],
                "feelslike_c": hour_data["feelslike_c"],
                "feelslike_f": hour_data["feelslike_f"],

                "windchill_c": hour_data["windchill_c"],
                "windchill_f": hour_data["windchill_f"],

                "heatindex_c": hour_data["heatindex_c"],
                "heatindex_f": hour_data["heatindex_f"],

                "dewpoint_c": hour_data["dewpoint_c"],
                "dewpoint_f": hour_data["dewpoint_f"],

                "will_it_rain": hour_data["will_it_rain"],
                "will_it_snow": hour_data["will_it_snow"],
                "chance_of_rain": hour_data["chance_of_rain"],
                "chance_of_snow": hour_data["chance_of_snow"],

                "is_day": hour_data["is_day"],
                
                "gust_mph": hour_data["gust_mph"],
                "gust_kph": hour_data["gust_kph"],
                
                "uv": hour_data["uv"],

                "visibility_km": hour_data["vis_km"],
                "visibility_miles": hour_data["vis_miles"]
            })

    current_date += timedelta(days=1)

csv_filename = "tokyo-mar-dec.csv"
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=all_forecasts[0].keys())
    writer.writeheader()
    writer.writerows(all_forecasts)

print(f"Hourly forecast data saved to {csv_filename}")
