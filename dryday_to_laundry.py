import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv() # will search for .env file in local folder and load variables 
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
API_KEY = WEATHER_API_KEY

def dryday_to_laundry(city, target_time):
    api_key = os.getenv("DRYDAY_API_KEY")
    if not api_key:
        raise ValueError("API key is missing. Please check your .env file.")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast_time = target_time + timedelta(days=1)
        
        # Check weather forecast for the next 24 hours from the target time
        for forecast in data['list']:
            forecast_dt = datetime.utcfromtimestamp(forecast['dt'])

            if forecast_dt >= target_time and forecast_dt <= forecast_time:
                 # If it rains during the specified time
                weather_description = forecast['weather'][0]['description']
                if 'rain' in weather_description.lower():
                    # Find the next time it will stop raining
                    for next_forecast in data['list']:
                        next_forecast_dt = datetime.utcfromtimestamp(next_forecast['dt'])
                        if next_forecast_dt > forecast_dt:
                            next_weather_description = next_forecast['weather'][0]['description']
                            if 'rain' not in next_weather_description.lower():
                                # Found the next time it will stop raining
                                stop_rain_time = next_forecast_dt.strftime("%Y-%m-%d %H:%M:%S")
                                return f"\033[31m\033[1m>>>It will rain at {forecast_dt}. It's NOT RECOMMENDED to hang laundry.\033[0m" \
                                       f"\033[93m\nThe next time you can hang laundry is at {stop_rain_time}.\033[0m"


        # If no rain found in the forecast period
        return      f"\033[32m\033[1m>>>No rain within 24 hours from the specified time. YOU CAN HANG LAUNDRY!\033[0m" \
                    f"\033[93m\nWeather details\n" \
                    f"___________________________\n" \
                    f"Temperature: {data['list'][0]['main']['temp']}°C\n" \
                    f"Humidity: {data['list'][0]['main']['humidity']}%\n" \
                    f"Wind Speed: {data['list'][0]['wind']['speed']} m/s\033[0m"

    else:
        return f"\033[31m\033[1mError {response.status_code}: Unable to fetch weather data for {city}\033[0m"

