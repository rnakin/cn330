import requests

def get_weather_by_city(city, api_key):
    # URL ของ OpenWeatherMap API สำหรับสภาพอากาศตามชื่อเมือง
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # ส่ง HTTP GET request
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # ดึงข้อมูลที่ต้องการจากผลลัพธ์
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']
        
        # แสดงข้อมูลสภาพอากาศ
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {weather_description}")
    else:
        print(f"Error {response.status_code}: Unable to fetch weather data for {city}")

if __name__ == "__main__":
    # ใส่ API Key ของคุณที่นี่
    api_key = "fdd3143d85fe49adb9448b7c17907b47"
    city = input("Enter city name: ")
    get_weather_by_city(city, api_key)
