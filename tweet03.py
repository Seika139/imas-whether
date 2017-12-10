#!/usr/bin/env python
# coding: utf-8
import os
import json
from requests_oauthlib import OAuth1Session
import requests
import urllib.request
import numpy.random as nmr

#Herokuの環境変数
AT = os.environ["ACCESS_TOKEN"]           # Access Token
AS = os.environ["ACCESS_TOKEN_SECRET"]    # Accesss Token Secert
CK = os.environ["CONSUMER_KEY"]           # Consumer Key
CS = os.environ["CONSUMER_SECRET"]        # Consumer Secret

#キャラクターの決定
idl_num = nmr.randint(0,3)

if idl_num == 0:
    import udsuki as idl
    p_num = nmr.randint(1,5)
    idl_photo = 'udsuki0{}.jpg'.format(p_num)
elif idl_num == 1:
    import rin as idl
    p_num = nmr.randint(1,5)
    idl_photo = 'rin.0{}jpg'.format(p_num)
elif idl_num == 2:
    import mio as idl
    p_num = nmr.randint(1,4)
    idl_photo = 'mio0{}.jpg'.format(p_num)

idl_photo = "pictures/" + idl_photo

#ツイートする文章の決定
tweeting_text = idl.f_text

#ここから下は雛型とおなじ
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# OAuth認証 セッションを開始
twitter = OAuth1Session(CK, CS, AT, AS)

# 画像投稿
files = {"media" : open(idl_photo , 'rb')}
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

print ("投稿できました！")
