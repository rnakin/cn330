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