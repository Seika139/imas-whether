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

#ループに用いるリスト
l_url = ["http://www.drk7.jp/weather/xml/04.xml","http://www.drk7.jp/weather/xml/13.xml","http://www.drk7.jp/weather/xml/27.xml","http://www.drk7.jp/weather/xml/40.xml"]
l_id = ["東部","東京地方","大阪府","福岡地方"]
l_area_name = ["仙台","東京","大阪","福岡"]

#ループの作成
for i in range(4):
    f_url = l_url[i]
    f_id = l_id[i]
    f_area_name = l_area_name[i]

    if i == 0:
        idl_num = nmr.randint(2)
        if idl_num == 0:
            import udsuki as idl
            p_num = nmr.randint(1,34)
            idl_photo = 'udsuki0{}.jpg'.format(p_num)

        elif idl_num == 1:
            import rin as idl
            p_num = nmr.randint(1,33)
            idl_photo = 'rin0{}.jpg'.format(p_num)

    elif i == 1:
        idl_num = nmr.randint(2)
        if idl_num == 0:
            import mio as idl
            p_num = nmr.randint(1,10)
            idl_photo = 'mio0{}.jpg'.format(p_num)

        elif idl_num == 1:
            import anzu as idl
            p_num = nmr.randint(1,36)
            idl_photo = 'anzu0{}.jpg'.format(p_num)

    elif i == 2:
        idl_num = nmr.randint(2)
        if idl_num == 0:
            import anastasia as idl
            p_num = nmr.randint(1,13)
            idl_photo = 'anastasia0{}.jpg'.format(p_num)

        elif idl_num == 1:
            import yuko as idl
            if "温泉" in idl.c_text:
                p_num = nmr.randint(1,3)
                idl_photo = 'yuko2{}.jpg'.format(p_num)
            else:
                p_num = nmr.randint(1,11)
                idl_photo = 'yuko0{}.jpg'.format(p_num)


    elif i == 3:
        idl_num = nmr.randint(1)
        if idl_num == 0:
            import miku as idl
            if "魚" in idl.c_text:
                idl_photo = "miku041,jpg"
            else:
                p_num = nmr.randint(1,38)
                idl_photo = 'miku0{}.jpg'.format(p_num)

    #最終的な画像のパスを指定
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