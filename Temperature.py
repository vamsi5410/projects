import requests
from pywebio.input import *
from pywebio.output import *

def fetch_weather_data(location, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/forecast/daily?lat=57&lon=-2.15&appid={API key}"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Adjust units as needed (e.g., metric, imperial)
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(data):
    if "main" in data and "weather" in data:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {data['name']} - Temperature: {temperature}°C, Humidity: {humidity}%, Conditions: {weather_description}")
    else:
        print("Location not found or data unavailable.")

def main():
    location = input("Enter a city or ZIP code: ")
    api_key = "YOUR_API_KEY"  # Get your API key from the weather service
    weather_data = fetch_weather_data(location, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
