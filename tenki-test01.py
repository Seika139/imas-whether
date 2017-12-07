#encoding:utf-8
import os
import json
from requests_oauthlib import OAuth1Session
import requests
import pprint
"""
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tokyo,jp')
print(r.status_code)
print(r.text)
"""

API_KEY = "ee84768ccca3c5ad082603b6a0567bfd"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
BASE_URL2 = "http://api.openweathermap.org/data/2.5/weather"



url5 = BASE_URL2 + "?q=Tokyo,jp&units=metric&APPID={}".format(API_KEY)
r5 = requests.get(url5)
w_d2 = r5.json()


def new_g_w():
    print(w_d2)


url4 = BASE_URL + "?q=Egotamachi,jp&units=metric&APPID={}".format(API_KEY)
r4 = requests.get(url4)
print(r4.status_code)
w_d =r4.json()

def get_weather1():
    print(w_d["city"],"\n"+"#"*35)
    for i in range(len(w_d["list"])):
        pprint.pprint(w_d["list"][i]["dt_txt"])
        pprint.pprint(w_d["list"][i]["main"]["humidity"])
        print("-"*35)

def get_weather2():
    pprint.pprint(w_d)


def get_weather3():
    print(w_d["main"])

"""
if __name__ == "__main__":
    num = int(input("push 1 or  or 3 or 4 or 5\n"))
    if num == 1:
        get_weather1()
    elif num == 2:
        get_weather2()
    elif num == 3:
        get_weather3()
    elif num == 4:
        new_g_w()
    else:
        pass
"""






"""
r2 = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
print(r2.status_code)
print(len(r2.text))
pprint.pprint(r2.json())
"""

import xml.etree.ElementTree as ET
def xml():
    r6 = requests.get('http://www.drk7.jp/weather/xml/13.xml')
    print(r6.status_code)
    print(r6.text)
    tree = ET.parse(r6,"rb")
    root = tree.getroot()




def get_weather(city):
    base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    url = "{}?city={}".format(base_url,city)
    r3 = requests.get(url)
    pprint.pprint(r3.json()["description"])
    print("_"*35)
    pprint.pprint(r3.json()["forecasts"])
    print("_"*35)
    pprint.pprint(r3.json()["location"])
    print("_"*35)

while 1:
    city_data = int(input("東京は1,大阪は3を押してください。それ以外を押すと終了します。"))
    print("###########################"*3)
    if city_data == 1:
        get_weather(130010)
    elif city_data == 3:
        get_weather(270000)
    elif city_data == 2:
        xml()
    else:
        break
