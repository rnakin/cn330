import argparse
import os
from datetime import datetime
from dotenv import load_dotenv
import requests
from ns import get_ip, is_ip
from power_advisor import get_power_advice, forecast_advice, calculate_power_cost
from take_things_out import take_things_out
from dryday_to_laundry import dryday_to_laundry

def load_environment_variables():
    """Load environment variables from .env file."""
    load_dotenv()
    return {
        "IPGEO_API_KEY": os.environ.get("IPGEO_API_KEY"),
        "WEATHER_API_KEY": os.environ.get("WEATHER_API_KEY"),
    }

def fetch_data(url, params):
    """Helper function to make GET requests."""
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    print(f"Error fetching data: {response.json().get('message')}")
    return None

def get_location_data(query, api_key):
    """Fetch location data using ipgeolocation.io API."""
    params = {"apiKey": api_key, "ip": query}
    return fetch_data("https://api.ipgeolocation.io/ipgeo", params)

def get_weather_data(lat, lon, api_key):
    """Fetch weather data using OpenWeatherMap API."""
    params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
    return fetch_data("https://api.openweathermap.org/data/2.5/weather", params)

def format_output(domain, location_data, weather_data):
    """Format the output for display."""
    time = datetime.now().strftime("%H:%M %Z")
    description = weather_data["weather"][0]["description"].capitalize()
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    city = location_data["city"]
    country = location_data["country_name"]
    timezone_offset = location_data["time_zone"]["offset"]

    domain = domain or "your location"
    return (f"It is {description} at {domain}.\n"
            f"Located at: {city}, {country}\n"
            f"Temperature: {temp}°C, Humidity: {humidity}%\n"
            f"{time} GMT {timezone_offset}")

def handle_list_option():
    """Handle the --list option."""
    print("Available services and APIs:")
    print("- ipgeolocation.io API for location data")
    print("- OpenWeatherMap API for current weather data")
    print("- Power advisor for energy consumption advice")

def handle_carry(query):
    if query:
        print( take_things_out(query))
    else:
        print("Error: Please provide a location.")
def handle_power_advice(query):
    """Handle the --power-advice option."""
    if query:
        print(get_power_advice(query))
    else:
        print("Error: Please provide a location.")

def handle_forecast_advice(query, days):
    """Handle the --forecast-advice option."""
    if query:
        print(forecast_advice(query, days=days))
    else:
        print("Error: Please provide a location.")

def handle_calculate_cost(rate, usage):
    """Handle the --calculate-cost option."""
    if rate and usage:
        print(calculate_power_cost(rate, usage))
    else:
        print("Error: Please provide both --rate and --usage.")

def handle_laundry(query):
    """Handle the --calculate-cost option."""
    if rate and usage:
        print(dryday_to_laundry(city, target_time, api_key=API_KEY))
    else:
        print("Error: Please provide both --rate and --usage.")

def handle_ip_option(query, api_keys):
    """Handle the --ip option."""
    if not is_ip(query):
        query = get_ip(query)  # Resolve domain name to IP if it's not already an IP
        if not query:
            print("Error: Unable to resolve domain to an IP address.")
            return

    location_data = get_location_data(query, api_keys["IPGEO_API_KEY"])
    if location_data:
        lat, lon = location_data["latitude"], location_data["longitude"]
        weather_data = get_weather_data(lat, lon, api_keys["WEATHER_API_KEY"])
        if weather_data:
            print(format_output(query, location_data, weather_data))
            return location_data.get("city", "Unknown city")



def main():
    api_keys = load_environment_variables()

    parser = argparse.ArgumentParser(
        description="HowIs: A CLI tool to check location and weather of a domain/IP."
    )
    parser.add_argument("query", nargs="?", type=str, help="Domain name, IPv4, or IPv6 address.")
    parser.add_argument("--list", action="store_true", help="List available services and APIs.")
    parser.add_argument("--power-advice", action="store_true", help="Get energy advice based on current weather.")
    parser.add_argument("--forecast-advice", action="store_true", help="Get forecast advice for energy consumption.")
    parser.add_argument("--calculate-cost", action="store_true", help="Calculate power costs based on device usage.")
    parser.add_argument("--rate", type=float, help="Electricity rate in USD/unit (for --calculate-cost).")
    parser.add_argument("--usage", type=str, help="Device usage in format 'Device:Hours,Device:Hours' (for --calculate-cost).")
    parser.add_argument("--days", type=int, help="Number of days to forecast (used with --forecast-advice).")
    parser.add_argument("--ip", action="store_true", help="Fetch current weather for the provided IP or domain.")
    parser.add_argument("--carry", action="store_true", help="Recommend Item that should be carry in the weather.")
    parser.add_argument("--laundry", action="store_true", help="Check if today is a suitable day for hanging laundry.")

    args = parser.parse_args()
    if args.ip:
        city_name = handle_ip_option(args.query, api_keys)  
        if city_name and args.power_advice:
            handle_power_advice(city_name)
        if city_name and args.forecast_advice:
            handle_forecast_advice(city_name, args.days)
        if city_name and args.carry:
            handle_carry(city_name)
    elif args.list:
        handle_list_option()
    elif args.power_advice:
        handle_power_advice(args.query)
    elif args.forecast_advice:
        handle_forecast_advice(args.query, args.days)
    elif args.calculate_cost:
        handle_calculate_cost(args.rate, args.usage)
    elif args.carry:
        handle_carry(args.query)

    # Handle --list option
    if args.list:
        print("Available services and APIs:")
        print("- ipgeolocation.io API for location data")
        print("- OpenWeatherMap API for current weather data")
        print("- Check what items you should take out today. eg, umbrella, hat.")
        print("- Check if it's a good day to hang laundry")
        return

    # Handle --take_things option
    if args.take_things:
        print()
        print("\033[1m\033[38;5;213mThis tool helps you prepare things before go out.\033[0m")
        print("\033[38;5;213m______________________________________________________________________\033[0m")
        
        city = input("Please enter the city (e.g., Bangkok): ").strip() 
        
        result = take_things_out(city)
        print(result)
        return


# Handle --laundry option
    if args.laundry:
        print()
        print("\033[1m\033[38;5;213mThis tool helps you decide if it's a suitable day for hanging laundry.\033[0m")
        print("\033[38;5;213m______________________________________________________________________\033[0m")

        city = input("Please enter the city (e.g. Bangkok): ").strip()  
        target_time_str = input("Please enter the time (YYYY-MM-DD HH:MM:SS) or ENTER if you want current time: ").strip()

        if not target_time_str:  # If no time is provided, use current time
            target_time = datetime.now()
            print("\033[38;5;213mNo time entered. Using current time: {}\033[0m".format(target_time.strftime("%Y-%m-%d %H:%M:%S")))
        else:
            try:
                target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("\033[31m\033[1mInvalid time format. Please use 'YYYY-MM-DD HH:MM:SS'.\033[0m")
                return

        result = dryday_to_laundry(city, target_time)
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
    main()
