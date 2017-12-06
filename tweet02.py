#!/usr/bin/env python
# coding: utf-8
import os
import json
from requests_oauthlib import OAuth1Session
import requests

AT = os.environ["ACCESS_TOKEN"]           # Access Token
AS = os.environ["ACCESS_TOKEN_SECRET"]    # Accesss Token Secert
CK = os.environ["CONSUMER_KEY"]           # Consumer Key
CS = os.environ["CONSUMER_SECRET"]        # Consumer Secret




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



tweeting_text = "こんばんは！"+time+"の天気予報です。\n天気は"+tenki+"\n最高気温は"+t_max+"度、最低気温は"+t_min+"です。"


url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# OAuth認証 セッションを開始
twitter = OAuth1Session(CK, CS, AT, AS)

# 画像投稿
files = {"media" : open('udsuki2.jpg', 'rb')}
req_media = twitter.post(url_media, files = files)

# レスポンスを確認
if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

# Media ID を取得
media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

# Media ID を付加してテキストを投稿
params = {'status': tweeting_text , "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

# 再びレスポンスを確認
if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")
