# Unified Command-Line Application: HowIs & Weather CLI

## Overview

**HowIs** and the **Weather CLI** are versatile command-line tools designed to provide real-time weather data, location details, and weather-based advice. These tools leverage APIs like **OpenWeatherMap** and **ipgeolocation.io** to deliver accurate and actionable information to users.

---

## Features

### Weather Feature: Take Things Out

This feature provides recommendations for items to bring based on weather conditions, temperature, and time of day in any city.

- Fetches real-time weather data:
  - Temperature (in Celsius)
  - Weather description (e.g., clear sky, rain)
  - Time of day (daytime or nighttime)
  - Current time in the city's time zone
- Provides recommendations for what to bring:
  - Jacket
  - Umbrella
  - Hat and sunscreen (for sunny daytime)

#### How to Use
1. Run the script:
   ```bash
   python main.py --take_things
   ```
2. Enter the name of the city when prompted.

#### Example Output
- **Rainy and cold day in London:**
  ```
  Please enter the city (e.g., Bangkok): London
  >>> You should take both umbrella and jacket with you!
  City Details
  ___________________________
  London is located in GB, with 0 GMT.
  The temperature of London right now is 8.50°C with light rain weather.
  ```
- **Sunny day in Bangkok:**
  ```
  >>> Don't forget your hat and sunscreen!
  City Details
  ___________________________
  Bangkok is located in TH, with +7 GMT.
  The temperature of Bangkok right now is 32.50°C with clear sky weather.
  ```

---

### Power Consumption Advisor CLI

A feature-rich command-line tool for weather-based power consumption advice, cost estimation, and energy usage forecasts.

#### Features

1. **Power Consumption Advice**
   - Get energy usage recommendations based on current weather conditions.
   - Subcommand: `power-advice <location>`

2. **Electricity Cost Calculation**
   - Calculate electricity cost based on device usage and electricity rate.
   - Subcommand: `calculate-cost <location>`
     - Options:
       - `--rate <electricity_rate>`: Specify the electricity rate (in USD/unit).
       - `--usage <device:hours>`: Specify device usage in the format `Device:Hours` (e.g., AC:4, Fan:6, Heater:10).

3. **Weather Forecast Advice**
   - Get power consumption advice for upcoming days based on weather forecasts.
   - Subcommand: `forecast-advice <location>`
     - Options:
       - `--days <number>`: Specify the number of days to forecast (default is all available data).

#### How to Use

1. Power Consumption Advice:
   ```bash
   python main.py --power-advice "Bangkok"
   ```
   **Output:**
   ```bash
   Power Consumption Advice for Bangkok:
    - Temperature: 30.5°C
    - Humidity: 60%
    - Weather: Partly cloudy
    - Advice: Use a fan instead of air conditioning to save energy.
   ```

2. Calculate Electricity Cost:
   ```bash
   python main.py --calculate-cost --rate 0.16 --usage "AC:8,Fan:5"
   ```
   **Output:**
   ```
   Power Consumption Cost Breakdown:
   - AC: 8.0 hrs/day, 12.00 kWh, 1.92 USD
   - Fan: 5.0 hrs/day, 0.35 kWh, 0.06 USD

   Total Cost: 1.98 USD/day
   ```

3. Forecast Advice:
   ```bash
   python main.py --forecast-advice "Bangkok" --days 4
   ```
   **Output:**
   ```
   Weather Forecast for Bangkok:
   2024-12-23: 23.05°C, Humidity 48%, Few clouds
   - Advice: No cooling needed. Keep warm naturally.
   2024-12-24: 25.94°C, Humidity 53%, Scattered clouds
   - Advice: Consider using a fan instead of AC.
   2024-12-25: 26.57°C, Humidity 51%, Broken clouds
   - Advice: Consider using a fan instead of AC.
   2024-12-26: 28.78°C, Humidity 53%, Overcast clouds
   - Advice: Consider using a fan instead of AC.
   ```

---

### HowIs: Weather & Location Finder

A command-line tool to determine the location and current weather of a domain name, IPv4/IPv6 address, or city name.

#### Features
- Fetch current location and weather for a domain, IP address, or city.
- Default input is a city (e.g., `London`) when no query is provided.
- Special handling for IP addresses with the `--ip` flag.
- List APIs and services used with the `--list` flag.
- Display weather description, temperature, and humidity for the specified location.

#### How to Use

1. Default Query:
   ```bash
   python main.py
   ```

2. Check Weather for a Domain:
   ```bash
   python main.py google.com
   ```

3. Check Weather for an IP Address:
   ```bash
   python main.py 8.8.8.8 --ip
   ```

4. List Available Services:
   ```bash
   python main.py --list
   ```

#### Example Outputs

- **Domain Name Query:**
  ```bash
  python main.py google.com
  ```
  **Output:**
  ```
  It is clear sky at google.com
  Located at: Mountain View, United States
  Temperature: 22°C, Humidity: 40%
  ```

- **IP Address Query:**
  ```bash
  python main.py 8.8.8.8 --ip
  ```
  **Output:**
  ```
  It is clear sky at 8.8.8.8
  Located at: Mountain View, United States
  Temperature: 22°C, Humidity: 40%
  ```

---

## Prerequisites

1. Python 3.7 or later installed.
2. API keys for:
   - [ipgeolocation.io](https://ipgeolocation.io/) (for location data).
   - [OpenWeatherMap](https://openweathermap.org/api) (for weather data).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/howis-cli.git
   cd howis-cli
   ```

2. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   IPGEO_API_KEY=your_ipgeolocation_api_key
   WEATHER_API_KEY=your_openweathermap_api_key
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

---

## Docker Support

### Build Docker Image
```bash
docker build -t howis-cli .
```

### Run Docker Container
```bash
docker run --env IPGEO_API_KEY=your_ipgeolocation_api_key \
           --env WEATHER_API_KEY=your_openweathermap_api_key \
           howis-cli google.com
```

### Use Docker Compose
1. Create a `docker-compose.yml` file:
   ```yaml
   version: '3.8'
   services:
     howis:
       build: .
       environment:
         - IPGEO_API_KEY=your_ipgeolocation_api_key
         - WEATHER_API_KEY=your_openweathermap_api_key
   ```

2. Start the container:
   ```bash
   docker-compose up
   ```

3. Run the application inside the container:
   ```bash
   docker-compose run howis google.com
   ```

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [ipgeolocation.io](https://ipgeolocation.io/)
- [OpenWeatherMap](https://openweathermap.org/)

