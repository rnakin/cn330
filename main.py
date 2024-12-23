import argparse
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from ns import get_ip ,is_ip
from power_advisor import get_power_advice, forecast_advice, calculate_power_cost  # นำเข้าฟังก์ชัน

load_dotenv() # will search for .env file in local folder and load variables 

# API Endpoints
IPGEO_API_URL = "https://api.ipgeolocation.io/ipgeo"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Fetch environment variables
IPGEO_API_KEY = os.environ.get("IPGEO_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def get_location_data(query):
    """Fetch location data using ipgeolocation.io API."""
    params = {"apiKey": IPGEO_API_KEY, "ip": query}
    response = requests.get(IPGEO_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching location data: {response.json().get('message')}")
        return None

def get_weather_data(lat, lon):
    """Fetch weather data using OpenWeatherMap API."""
    params = {"lat": lat, "lon": lon, "appid": WEATHER_API_KEY, "units": "metric"}
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.json().get('message')}")
        return None

def format_output(domain, location_data, weather_data):
    """Format and display the output."""
    time = datetime.now().strftime("%H:%M %Z")
    description = weather_data["weather"][0]["description"].capitalize()
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    city = location_data["city"]
    country = location_data["country_name"]
    if domain is None:
        domain = "your location"
    text = f""" 
    It is {description} at {domain}.
    Located at: {city}, {country}
    Temperature: {temp}°C, Humidity: {humidity}%
    {time} GMT {location_data['time_zone']['offset']}
    """

    return text

def main():

    parser = argparse.ArgumentParser(
        description="HowIs: A CLI tool to check location and weather of a domain/IP."
    )
    parser.add_argument(
        "query",
        nargs="?",
        type=str,
        help="Domain name, IPv4, or IPv6 address. Example: google.com or 8.8.8.8",
    )
    parser.add_argument(
        "--now", action="store_true", help="Fetch current weather (default behavior)."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available services and APIs used in this application.",
    )
    parser.add_argument(
        "--test", action="store_true", help="testing"
    )
    parser.add_argument(
        "--power-advice", action="store_true", help="Get energy advice based on current weather."
    )
    parser.add_argument(
        "--forecast-advice", action="store_true", help="Get forecast advice for energy consumption."
    )
    parser.add_argument(
        "--calculate-cost", action="store_true", help="Calculate power costs based on device usage."
    )
    parser.add_argument(
        "--rate", type=float, help="Electricity rate in USD/unit (for --calculate-cost)."
    )
    parser.add_argument(
        "--usage", type=str, help="Device usage in format 'Device:Hours,Device:Hours' (for --calculate-cost)."
    )
    parser.add_argument(
        "--days", type=int, help="Number of days to forecast (used with --forecast-advice)."
    )
    args = parser.parse_args()

    # Handle --list option
    if args.list:
        print("Available services and APIs:")
        print("- ipgeolocation.io API for location data")
        print("- OpenWeatherMap API for current weather data")
        return

    # Handle --power-advice option
    if args.power_advice:
        if args.query:
            print(get_power_advice(args.query))
        else:
            print("Error: Please provide a location.")
        return

    # Handle --forecast-advice option
    if args.forecast_advice:
        if args.query:
            days = args.days if args.days else None  # ใช้ args.days ถ้ามีการกำหนด
            print(forecast_advice(args.query, days=days))
        else:
            print("Error: Please provide a location.")
        return

    # Handle --calculate-cost option
    if args.calculate_cost:
        if args.rate and args.usage:
            print(calculate_power_cost(args.rate, args.usage))
        else:
            print("Error: Please provide both --rate and --usage.")
        return

    # Get location data
    if is_ip(args.query):
        location_data = get_location_data(args.query)
    else:
        location_data = get_location_data(get_ip(args.query))
    if not location_data:
        return

    # Get weather data
    lat, lon = location_data["latitude"], location_data["longitude"]
    weather_data = get_weather_data(lat, lon)
    if not weather_data:
        return

    # Format output
    text = format_output(args.query, location_data, weather_data)
    print(text)

if __name__ == "__main__":
    main()