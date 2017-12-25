#encoding:utf-8

#モジュールのインポート
import xml.etree.ElementTree as ET
import urllib.request as ur
from tweet04 import f_id,f_url,f_area_name



#urlを入れる
url = f_url
req = ur.Request(url)

#データの取得
with ur.urlopen(req) as response:
    XmlData = response.read()
root = ET.fromstring(XmlData)

#それぞれの値の用意
area = root.findall(".//area[@id={}]".format(f_id))
for youso in area:
    place = f_area_name
    day1 = youso.find("info")
    reporting_date = day1.get("date")
    weather = day1[0].text
    weather_id = day1[1].text
    kion_list = day1.findall(".//range")
    kousuikakuritsu = day1.findall(".//period")
    kion_box = []
    for kion in kion_list:
        kion_box.append(kion.text)
    jikantai = []
    rain = []
    for i in kousuikakuritsu:
        jikantai.append(i.get("hour"))
        rain.append(int(i.text))

if __name__ == "__main__":
    print("このモジュールで{}の天気情報を取得しています。".format(place))
