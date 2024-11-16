import requests
from html import unescape
from bs4 import BeautifulSoup

def get_weather_data(soup, class_name, default_text):
    element = soup.find(class_=class_name)
    if element:
        return unescape(element.get_text(strip=True))
    return default_text

def get_weather(city):
    try:
        city_query = city.replace(" ", "+")
        url = f"https://www.google.com/search?q=weather+{city_query}&hl=en"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        location_text = get_weather_data(soup, "BNeawe tAd8D AP7Wnd", "Location data not found")
        temperature_text = get_weather_data(soup, "BNeawe iBp4i AP7Wnd", "Temperature data not found")
        condition_text = get_weather_data(soup, "BNeawe tAd8D AP7Wnd", "Condition data not found")

        return f"Location: {location_text}\nTemperature: {temperature_text}\nCondition: {condition_text}"

    except Exception as e:
        return f"Error: Could not fetch weather data. Details: {str(e)}"
