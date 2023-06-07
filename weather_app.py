# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lDMzp5QHyZIhUYmle7LT-Zx_9c5oL2zP
"""

import requests
import json

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def display_weather(weather_data, city):
    if weather_data['cod'] == 200:
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        visibility = weather_data['visibility'] / 1000  # Convert visibility from meters to kilometers
        sunrise = weather_data['sys']['sunrise']
        sunset = weather_data['sys']['sunset']

        print(f"Weather Information for {city}:")
        print(f"Temperature: {temperature_celsius:.1f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Visibility: {visibility} km")
        print(f"Sunrise: {convert_timestamp(sunrise)}")
        print(f"Sunset: {convert_timestamp(sunset)}")
    else:
        print(f"Weather information for {city} not found.")

def convert_timestamp(timestamp):
    import datetime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def weather_app():
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'fab9077fb4b0425e56ed6c89f3e230be'

    choice = input("Enter '1' to check weather for one city or '2' to compare weather for two cities: ")
    if choice == '1':
        city = input("Enter a city name: ")
        weather_data = get_weather(api_key, city)
        display_weather(weather_data, city)
    elif choice == '2':
        city1 = input("Enter the first city name: ")
        city2 = input("Enter the second city name: ")

        weather_data1 = get_weather(api_key, city1)
        weather_data2 = get_weather(api_key, city2)

        display_weather(weather_data1, city1)
        print("----------------------------------")
        display_weather(weather_data2, city2)
    else:
        print("Invalid choice.")

weather_app()