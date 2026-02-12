import requests

def fetch_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise RuntimeError(response.json().get("message", "API error"))

    return response.json()
