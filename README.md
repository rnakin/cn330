# Group 2 Project : Weather Command-line Application

# Weather Feature: Take Things Out

This feature allows you to determine what items to bring with you based on the weather conditions, temperature, and time of day in any city. It uses the OpenWeatherMap API to fetch real-time weather data.

## Features
- Fetches real-time weather data, including:
  - Temperature (in Celsius)
  - Weather description (e.g., clear sky, rain)
  - Time of day (daytime or nighttime)
  - Current time in the city's time zone
- Provides recommendations for what to bring:
  - Jacket
  - Umbrella
  - Hat and sunscreen (for sunny daytime)

## How to Run
1. Run the script using:
   ```bash
   python main.py --take_things
   ```
2. Enter `"City name"` of the city you want to check.

## Output
If successful, the script will display:
- Recommendations for items to bring.
- City details, including temperature, country, and weather description.

### Example Output
#### Scenario: Rainy and cold day in London
```
Please enter the city (e.g., Bangkok): London
>>> You should take both umbrella and jacket with you! Don't forget your hat and sunscreen!
City Details
___________________________
London is located in GB, with 0 GMT.
The temperature of London right now is 8.50°C with light rain weather.
```

#### Scenario: Sunny day in Bangkok
```
>>> Don't forget your hat and sunscreen!
City Details
___________________________
Bangkok is located in TH, with +7 GMT.
The temperature of Bangkok right now is 32.50°C with clear sky weather.
```

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE.
# Power Consumption Advisor CLI

Power Consumption Advisor CLI is a lightweight command-line application that provides weather-based power consumption advice, cost estimation, and energy usage forecasts. This application is built using Python and leverages the OpenWeatherMap API for weather data.

---

## Features

### 1. **Power Consumption Advice**

- Get energy usage recommendations based on current weather conditions.
- Subcommand: `power-advice <location>`

### 2. **Electricity Cost Calculation**

- Calculate electricity cost based on device usage and electricity rate.
- Subcommand: `calculate-cost <location>`
  - Options:
    - `--rate <electricity_rate>`: Specify the electricity rate (in USD/unit).
    - `--usage <device:hours>`: Specify device usage in the format `Device:Hours` (e.g., AC:4, Fan:6, Heater:10).

### 3. **Weather Forecast Advice**

- Get power consumption advice for upcoming days based on weather forecasts.
- Subcommand: `forecast-advice <location>`
  - Options:
    - `--days <number>`: Specify the number of days to forecast (default is all available data).

## How to run command

1. Power Consumption Advice:

   ```bash
   python main.py --power-advice "Bangkok"
   ```

   Output:

   ```bash
   Power Consumption Advice for Bangkok:
    - Temperature: 30.5°C
    - Humidity: 60%
    - Weather: Partly cloudy
    - Advice: Use a fan instead of air conditioning to save energy.
    ```

1. Calculate Electricity Cost:

    ```bash
    python main.py --calculate-cost --rate 0.16 --usage "AC:8,Fan:5"
    ```

    Output:

    ```
    Power Consumption Cost Breakdown:
    - AC: 8.0 hrs/day, 12.00 kWh, 1.92 USD
    - Fan: 5.0 hrs/day, 0.35 kWh, 0.06 USD

    Total Cost: 1.98 USD/day
    ```

1. Forecast Advice:

    ```bash
    python main.py --forecast-advice "Bangkok" --days 4
    ```

    Output:

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
