import requests

API_KEY = "ee84768ccca3c5ad082603b6a0567bfd"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
BASE_URL2 = "http://api.openweathermap.org/data/2.5/weather"

url4 = BASE_URL + "?q=Toyko,jp&units=metric&APPID={}".format(API_KEY)
r4 = requests.get(url4)
w_d =r4.json()


time = w_d["list"][4]["dt_txt"]
tenki = w_d["list"][4]["weather"]["description"]
t_max = w_d["list"][4]["main"]["temp_max"]
t_min = w_d["list"][4]["main"]["temp_min"]
