from datetime import datetime as dt, timezone, timedelta
import requests

# main function
def take_things_out(city, api_key="9629b97c0926236b2c767c4c09ec7086"):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    url = f"{BASE_URL}appid={api_key}&q={city}&units=metric"
    response = requests.get(url).json()

    # Get necessary data from API
    if response.get("cod") == 200:
        weather = response["weather"][0]["main"]
        weather_desc = response["weather"][0]["description"]
        temp_celsius = response["main"]["temp"]
        timezone_sec = response["timezone"]
        local_time = dt.now(timezone(timedelta(seconds=timezone_sec))).strftime('%H:%M:%S')
        country = response["sys"]["country"]
        is_daytime = (
            response["sys"]["sunrise"]
            <= int(dt.now().timestamp())
            <= response["sys"]["sunset"]
        )

        # Check what to take out, depends on weather, temperature, and time
        if weather in ["Thunderstorm", "Drizzle", "Rain"]:
            jacket_and_umbrella = "both" if temp_celsius < 10 else "umbrella"
        elif weather == "Snow":
            jacket_and_umbrella = "jacket"
        else:
            jacket_and_umbrella = "jacket" if temp_celsius < 10 else "none"

        if is_daytime:
            if weather_desc.lower() in ["clear sky", "few clouds", "scattered clouds"]:
                sunscreen_and_hat = "yes"
            else:
                sunscreen_and_hat = "no"
        else:
            sunscreen_and_hat = "no"

        recommend = []
        if jacket_and_umbrella == "both" :
            recommend.append(f"\033[32m\033[1m>>> You should take both umbrella and jacket with you!\033[0m")
        elif jacket_and_umbrella != "none" :
            recommend.append(f"\033[32m\033[1m>>> You should take {jacket_and_umbrella} with you!\033[0m")
        if sunscreen_and_hat == "yes":
            recommend.append("\033[32m\033[1mDon't forget your hat and sunscreen!\033[0m")
            
        result = (
            (" ".join(recommend) if recommend else "\033[32m\033[1m>>> You can go out without any worries!\033[0m") +
            f"\033\n[93mCity Details\033[0m\n"
            f"\033[93m___________________________\033[0m\n"
            f"\033[93m{city} is located in {country}, with local time {local_time} and {int(timezone_sec / 3600)} GMT.\033[0m\n"
            f"\033[93mThe temperature of {city} right now is {temp_celsius:.2f}°C with {weather_desc} weather.\033[0m\n"
        )
        
        return result

    else:
        return f"\033[32m\033[1m>>> Error {response.get('cod')}: City {city} not found or API request failed.\033[0m"
