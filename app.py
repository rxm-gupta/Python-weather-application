import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather data for a given city using the OpenWeatherMap API
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use metric units (Celsius)
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data):
    """
    Format and display weather information
    """
    if not weather_data:
        return
    
    # Extract relevant information
    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    timestamp = weather_data["dt"]
    date_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    # Display the information
    print("\n" + "="*50)
    print(f"Weather in {city}, {country}")
    print("="*50)
    print(f"Date and Time: {date_time}")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("="*50 + "\n")

def main():
    print("Welcome to the Weather App!")
    print("Enter 'quit' to exit the application.")
    
    while True:
        city = input("\nEnter city name: ")
        
        if city.lower() == "quit":
            print("Thank you for using the Weather App. Goodbye!")
            break
        
        weather_data = get_weather(city)
        
        if weather_data:
            display_weather(weather_data)
        else:
            print(f"Could not retrieve weather data for {city}.")

if __name__ == "__main__":
    if not API_KEY:
        print("Error: No API key found. Please set the WEATHER_API_KEY environment variable.")
        print("You can get a free API key from https://openweathermap.org/api")
    else:
        main()
