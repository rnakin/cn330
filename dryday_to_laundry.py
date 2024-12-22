import requests
from datetime import datetime, timedelta

def dryday_to_laundry(city, target_time, api_key="fdd3143d85fe49adb9448b7c17907b47"):
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
                   return f"\033[31m\033[1m>>>It will rain at {forecast_dt}. It's NOT RECOMMENDED to hang laundry.\033[0m"


        # If no rain found in the forecast period
        return      f"\033[32m\033[1m>>>No rain within 24 hours from the specified time. YOU CAN HANG LAUNDRY!\033[0m" \
                    f"\033[93m\nWeather details\n" \
                    f"___________________________\n" \
                    f"Temperature: {data['list'][0]['main']['temp']}°C\n" \
                    f"Humidity: {data['list'][0]['main']['humidity']}%\n" \
                    f"Wind Speed: {data['list'][0]['wind']['speed']} m/s\033[0m"

    else:
        return f"\033[31m\033[1mError {response.status_code}: Unable to fetch weather data for {city}\033[0m"

