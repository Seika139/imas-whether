#encoding:utf-8
import os
import json
from requests_oauthlib import OAuth1Session
import requests
import pprint


#openweathermap

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


url4 = BASE_URL + "?q=Tokyo,jp&units=metric&APPID={}".format(API_KEY)
r4 = requests.get(url4)
print(r4.status_code)
w_d =r4.json()

def get_weather1():
    print(w_d["city"],"\n"+"#"*35)
    for i in range(min(10,len(w_d["list"]))):
        print("日時:",w_d["list"][i]["dt_txt"])
        print("湿度:",w_d["list"][i]["main"]["humidity"])
        print("気温:",w_d["list"][i]["main"]["temp"])
        try:
            print("降水確率:",w_d["list"][i]["rain"])
        except:
            print("にゃーー")
        print("-"*35)

def get_weather2():
    pprint.pprint(w_d)


def get_weather3():
    for i in range(len(w_d["list"])):
        pprint.pprint(w_d["list"][i]["main"])

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
import urllib.request as ur
url = "http://www.drk7.jp/weather/xml/13.xml"
req = ur.Request(url)

with ur.urlopen(req) as response:
    XmlData = response.read()

root = ET.fromstring(XmlData)
print("以下はxmlの天気予報")
print(root.tag,root.attrib)

for child in root:
    print(child.tag, child.attrib,child.text)



area = root.findall(".//area[@id='東京地方']")
for youso in area:
    print(youso.get("id"))
    info = youso.findall("info")
    for c in info:
        print(c.get("date"))
        print("天気は",c[0].text)
        kion = c.findall(".//range")
        kousuikakuritu = c.findall(".//period")
        for i in kion:
            print(i.get('centigrade'),i.text)
        for i in kousuikakuritu:
            print(i.get("hour"),"時の降水確率は",i.text,"%です")

        print("_"*35)
print("&"*40)


"""とー結
print("#$"*35)
r8 = requests.get("http://www.drk7.jp/weather/xml/13.xml")
r9 = r8.text.encoding("utf_8")
print(r9)
"""


def xml():
    r6 = requests.get('http://www.drk7.jp/weather/xml/13.xml')
    print(r6.status_code)
    print(r6.text)
    tree = ET.parse(r6,)
    root = tree.getroot()




#livedoorの天気予報

def get_weather(city):
    base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    url = "{}?city={}".format(base_url,city)
    r3 = requests.get(url)
    """
    pprint.pprint(r3.json()["description"])
    print("_"*35)
    pprint.pprint(r3.json()["forecasts"])
    print("_"*35)
    pprint.pprint(r3.json()["location"])
    print("_"*35)
    """
    pprint.pprint(r3.json())

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
