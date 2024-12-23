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
