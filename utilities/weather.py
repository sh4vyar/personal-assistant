import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=%l:+%c+%t"
        response = requests.get(url)
        response.raise_for_status()

        return response.text.strip()
    except Exception as e:
        return f"Error: Could not fetch weather data. Details: {str(e)}"