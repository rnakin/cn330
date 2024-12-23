import requests

API_KEY = "44c5e66627efa3057184a1b9ede5618b"

def fetch_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data: {response.status_code}")

def fetch_forecast(location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch forecast data: {response.status_code}")

def get_power_advice(location, show_temp=False, show_humidity=False):
    weather_data = fetch_weather(location)
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0].get("description", "No description")
    
    advice = f"Power Consumption Advice for {location}:\n"
    if show_temp and not show_humidity:
        advice += f"- Temperature: {temp}°C\n"
    elif show_humidity and not show_temp:
        advice += f"- Humidity: {humidity}%\n"
    elif show_temp and show_humidity:
        advice += f"- Temperature: {temp}°C\n"
        advice += f"- Humidity: {humidity}%\n"
    else:
        advice += f"- Temperature: {temp}°C\n"
        advice += f"- Humidity: {humidity}%\n"
        advice += f"- Weather: {description.capitalize()}\n"

    if temp > 35:
        advice += "- Advice: Use air conditioning during the hottest hours.\n"
    elif temp > 25:
        advice += "- Advice: Consider using a fan instead of AC.\n"
    else:
        advice += "- Advice: No cooling needed. Keep warm naturally.\n"
    return advice

def calculate_power_cost(rate, usage):
    power_data = {"AC": 1.5, "Fan": 0.07, "Heater": 2.0}
    usage_data = {item.split(":")[0]: float(item.split(":")[1]) for item in usage.split(",")}

    total_cost = 0
    breakdown = f"Power Consumption Cost Breakdown:\n"

    for device, hours in usage_data.items():
        if device in power_data:
            energy = power_data[device] * hours
            cost = energy * rate
            breakdown += f"- {device}: {hours} hrs/day, {energy:.2f} kWh, {cost:.2f} USD\n"
            total_cost += cost

    return breakdown + f"\nTotal Cost: {total_cost:.2f} USD/day"

def forecast_advice(location, days=None):
    forecast_data = fetch_forecast(location)
    if "list" not in forecast_data or len(forecast_data["list"]) == 0:
            return f"No forecast data available for {location}."

    advice = f"Weather Forecast for {location}:\n"
    max_entries = len(forecast_data["list"])  # Default to all entries

    if days:
        max_entries = min(days * 8, max_entries)  # 1 day = 8 entries (3-hour intervals)

    for i in range(0, max_entries, 8):  # Step by 8 for daily data
        day_data = forecast_data["list"][i]
        date = day_data["dt_txt"].split(" ")[0]
        temp = day_data["main"]["temp"]
        humidity = day_data["main"]["humidity"]
        description = day_data["weather"][0]["description"]

        if temp > 35:
                energy_advice = "Use air conditioning during the hottest hours."
        elif temp > 25:
                energy_advice = "Consider using a fan instead of AC."
        else:
                energy_advice = "No cooling needed. Keep warm naturally."

        advice += f"{date}: {temp}°C, Humidity {humidity}%, {description.capitalize()}\n"
        advice += f"- Advice: {energy_advice}\n"

    return advice

