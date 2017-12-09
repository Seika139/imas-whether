# coding: utf_8

import datetime
today = datetime.datetime.today().strftime("%Y/%m/%d")

import requests
url = 'http://www.drk7.jp/weather/xml/13.xml'
response = requests.get(url)

import xml.etree.ElementTree as ET
root = ET.fromstring(response.content)

# Get rainfallchance of North Yokohama
# Time: 12h - 18h and 18h - 24h
print(root)

for area in root.iter('area'):
    if area.get('id').encode('utf_8') == '東京地方':
        for info in area.findall('info'):
            if info.get('date') == today:
                rainfallchance = info.find('rainfallchance')
                for period in rainfallchance.findall('period'):
                    hour = period.get('hour')
                    if hour == '12-18' or hour == '18-24':
                        print (hour + 'h ' + period.text + '%')
