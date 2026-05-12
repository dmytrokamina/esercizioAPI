import os
from dotenv import load_dotenv

load_dotenv(override=True)

API_key = os.getenv('api_key')


import requests

def get_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric'
    res = requests.get(url)
    data = res.json()
    return data

# Bologna: lat=44.518009, lon=11.361852
get_weather(44.518009, 11.361852)
