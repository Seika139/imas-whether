#!/usr/bin/env python
# coding: utf-8

import os
import json
from requests_oauthlib import OAuth1Session

#Herokuの環境変数
AT = os.environ["ACCESS_TOKEN"]           # Access Token
AS = os.environ["ACCESS_TOKEN_SECRET"]    # Accesss Token Secert
CK = os.environ["CONSUMER_KEY"]           # Consumer Key
CS = os.environ["CONSUMER_SECRET"]        # Consumer Secret


the_text = "プロデューサーのみなさんこんばんは、千川ちひろです。\n"
the_text += "「デレマス朝の天気予報」に続き、「デレマス夜の天気予報」が始まります！\n"
the_text += "夜の天気予報は予報地点が増える上、新たに"
the_text += "４人のアイドルが追加されました♪\n今後も天気予報をしっかり見て、お仕事頑張ってくださいね！\n#デレマス夜の天気予報"


url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# OAuth認証 セッションを開始
twitter = OAuth1Session(CK, CS, AT, AS)

# 画像投稿
files = {"media" : open('pictures/chihiro01.jpg', 'rb')}
req_media = twitter.post(url_media, files = files)

# レスポンスを確認
if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

# Media ID を取得
media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

# Media ID を付加してテキストを投稿
params = {'status': the_text , "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

# 再びレスポンスを確認
if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")
