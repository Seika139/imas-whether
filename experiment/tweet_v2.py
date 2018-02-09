# coding: utf-8
import os
import json
from requests_oauthlib import OAuth1Session
import requests
import urllib.request
import numpy.random as nmr
import time

#実行する時間の取得
import datetime as dt
xd = dt.datetime.today()
xdj = xd + dt.timedelta(hours=9) #Herokuでは時間帯がUTCなので9時間後にずらす
xh = xdj.hour
if xh >= 0 and xh <= 12: x_num = 0
else: x_num = 1

#Herokuの環境変数
AT = os.environ["ACCESS_TOKEN"]           # Access Token
AS = os.environ["ACCESS_TOKEN_SECRET"]    # Accesss Token Secert
CK = os.environ["CONSUMER_KEY"]           # Consumer Key
CS = os.environ["CONSUMER_SECRET"]        # Consumer Secret

#予報するアイドルの番号の決定（被りが発生しないようにする）
l_idl_num = nmr.randint(0,11,4)
while l_idl_num[0] == l_idl_num[1]:
    l_idl_num[1] = nmr.randint(7)
while l_idl_num[2] in l_idl_num[:2]:
    l_idl_num[2] =  nmr.randint(7)
while l_idl_num[3] in l_idl_num[:3]:
    l_idl_num[3] =  nmr.randint(7)

#ループの作成
for i in range(4):
    import gt_v2
    if i == 0:
        gt = gt_v2.Get_tenki("http://www.drk7.jp/weather/xml/04.xml",'東部',"仙台")
    elif i == 1:
        gt = gt_v2.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',"東京")
    elif i == 2:
        gt = gt_v2.Get_tenki("http://www.drk7.jp/weather/xml/27.xml",'大阪府',"大阪")
    elif i == 3:
        gt = gt_v2.Get_tenki("http://www.drk7.jp/weather/xml/40.xml",'福岡地方',"福岡")


    idl_num = l_idl_num[i]
    if idl_num == 0:
        import udsuki_v2
        udsuki = udsuki_v2.Udsuki(gt.gt_box_array[x_num],x_num)
        tweeting_text = udsuki.f_text
        if "海" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'udsuki04{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,32)
            idl_photo = 'udsuki0{}.jpg'.format(p_num)

    elif idl_num == 1:
        import rin_v2
        rin = rin_v2.Rin(gt.gt_box_array[x_num],x_num)
        tweeting_text = rin.f_text
        if "海" in tweeting_text:
            idl_photo = 'rin041.jpg'
        else:
            p_num = nmr.randint(1,32)
            idl_photo = 'rin0{}.jpg'.format(p_num)

    elif idl_num == 2:
        import mio_v2
        mio = mio_v2.Mio(gt.gt_box_array[x_num],x_num)
        tweeting_text = mio.f_text
        p_num = nmr.randint(1,10)
        idl_photo = 'mio0{}.jpg'.format(p_num)

    elif idl_num == 3:
        import anzu_v2
        anzu = anzu_v2.Anzu(gt.gt_box_array[x_num],x_num)
        tweeting_text = anzu.f_text
        p_num = nmr.randint(1,36)
        idl_photo = 'anzu0{}.jpg'.format(p_num)

    elif idl_num == 4:
        import anastasia_v2
        anastasia = anastasia_v2.Anastasia(gt.gt_box_array[x_num],x_num)
        tweeting_text = anastasia.f_text
        p_num = nmr.randint(1,13)
        idl_photo = 'anastasia0{}.jpg'.format(p_num)

    elif idl_num == 5:
        import yuko_v2
        yuko = yuko_v2.Yuko(gt.gt_box_array[x_num],x_num)
        tweeting_text = yuko.f_text
        if "温泉" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'yuko2{}.jpg'.format(p_num)
        elif "ビーム" in tweeting_text: idl_photo = 'yuko010.jpg'
        else:
            p_num = nmr.randint(1,11)
            idl_photo = 'yuko0{}.jpg'.format(p_num)

    elif idl_num == 6:
        import miku_v2
        miku = miku_v2.Miku(gt.gt_box_array[x_num],x_num)
        tweeting_text = miku.f_text
        if "魚" in tweeting_text:
            idl_photo = "miku041.jpg"
        else:
            p_num = nmr.randint(1,38)
            idl_photo = 'miku0{}.jpg'.format(p_num)

    elif idl_num == 7:
        import yoshino_v2
        yoshino = yoshino_v2.Yoshino(gt.gt_box_array[x_num],x_num)
        tweeting_text = yoshino.f_text
        if "桜" or "紗枝" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'yoshino3{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,25)
            idl_photo = 'yoshino{}.jpg'.format(p_num)

    elif idl_num == 8:
        import arisu_v2
        arisu = arisu_v2.Arisu(gt.gt_box_array[x_num],x_num)
        tweeting_text = arisu.f_text
        if "イチゴ" or "いちご" in tweeting_text:
            p_num = nmr.randint(1,6)
            idl_photo = 'arisu_str{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,24)
            idl_photo = 'arisu{}.jpg'.format(p_num)

    elif idl_num == 9:
        import momoka_v2
        momoka = momoka_v2.Momoka(gt.gt_box_array[x_num],x_num)
        tweeting_text = momoka.f_text
        if "夜更かし" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'momoka_yofukashi{}.jpg'.format(p_num)
        elif "紅茶" or "ローズヒップティー" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'momoka_tea{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,31)
            idl_photo = 'momoka{}.jpg'.format(p_num)

    elif idl_num == 10:
        import fumika_v2
        fumika = fumika_v2.Fumika(gt.gt_box_array[x_num],x_num)
        tweeting_text = fumika.f_text
        if "ナイトプール" in tweeting_text:
            idl_photo = 'fumika27.jpg'
        else:
            p_num = nmr.randint(1,29)
            idl_photo = 'fumika{}.jpg'.format(p_num)

    #最終的な画像のパスを指定
    idl_photo = "pictures/" + idl_photo


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

    #連投防止のための一時停止
    if i <=2: time.sleep(30)

"""
gentle-crag-58603　の　tweet03.py を動かす時
heroku run python tweet03.py --app gentle-crag-58603
"""
