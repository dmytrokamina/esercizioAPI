import os
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv('api_key')


import requests
from datetime import datetime , timedelta


def get_hist_data(lat,lon,start):
    url_coord = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={'part'}&appid={'api_key'}'
    res = requests.get(url_coord)
    data = res.json()
    return data
    # temp = []
    # for hour in data["hourly"]:
    #     t = hour["temp"]
    #     temp.append(t)     
    # return data , temp


get_hist_data(11.371151787523646,44.508646872523734,datetime.now())
