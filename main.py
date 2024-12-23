import argparse
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
<<<<<<< HEAD
from ns import get_ip, is_ip
from dryday_to_laundry import dryday_to_laundry

load_dotenv()  # will search for .env file in local folder and load variables 
=======
from ns import get_ip ,is_ip
from take_things_out import take_things_out

load_dotenv() # will search for .env file in local folder and load variables 
>>>>>>> 5ae8c0775dccbfae0801b7d60e9b84bcd090b3db

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
<<<<<<< HEAD
    return text

def main():
    parser = argparse.ArgumentParser(description="HowIs: A CLI tool to check location and weather of a domain/IP.")
    parser.add_argument(
        "query", nargs="?", type=str, help="Domain name, IPv4, or IPv6 address. Example: google.com or 8.8.8.8"
=======

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
>>>>>>> 5ae8c0775dccbfae0801b7d60e9b84bcd090b3db
    )
    parser.add_argument(
        "--now", action="store_true", help="Fetch current weather (default behavior)."
    )
    parser.add_argument(
<<<<<<< HEAD
        "--list", action="store_true", help="List available services and APIs used in this application."
    )
    parser.add_argument(
        "--laundry", action="store_true", help="Check if it's a good day to hang laundry."
=======
        "--list",
        action="store_true",
        help="List available services and APIs used in this application.",
    )
    parser.add_argument(
        "--take_things", action="store_true", help="Check what items you should take out today. eg, umbrella, hat."
>>>>>>> 5ae8c0775dccbfae0801b7d60e9b84bcd090b3db
    )
    args = parser.parse_args()

    # Handle --list option
    if args.list:
        print("Available services and APIs:")
        print("- ipgeolocation.io API for location data")
        print("- OpenWeatherMap API for current weather data")
<<<<<<< HEAD
        print("- Check if it's a good day to hang laundry")
        return

    # Handle --laundry option
    if args.laundry:
        print()
        print("\033[1m\033[38;5;213mThis tool helps you decide if it's a suitable day for hanging laundry.\033[0m")
        print("\033[38;5;213m______________________________________________________________________\033[0m")

        city = input("Please enter the city (e.g., Bangkok): ").strip()  
        target_time_str = input("Please enter the time (YYYY-MM-DD HH:MM:SS): ").strip()
        
        try:
            target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("\033[31m\033[1mInvalid time format. Please use 'YYYY-MM-DD HH:MM:SS'.\033[0m")
            return
        
        result = dryday_to_laundry(city, target_time)
=======
        print("- Check what items you should take out today. eg, umbrella, hat.")
        return
    
    # Handle --take_things option
    if args.take_things:
        print()
        print("\033[1m\033[38;5;213mThis tool helps you prepare things before go out.\033[0m")
        print("\033[38;5;213m______________________________________________________________________\033[0m")
        
        city = input("Please enter the city (e.g., Bangkok): ").strip() 
        
        result = take_things_out(city)
>>>>>>> 5ae8c0775dccbfae0801b7d60e9b84bcd090b3db
        print(result)
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
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 5ae8c0775dccbfae0801b7d60e9b84bcd090b3db
