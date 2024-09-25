# using python libraries

import requests

API_KEY = "ce506afc8dc7a9ba850c1fca46234e5a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Please enter the city you wish to know the weather: ").lower()

def get_weather(city):
    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(request_url)
    
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Print the weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")

get_weather(city)