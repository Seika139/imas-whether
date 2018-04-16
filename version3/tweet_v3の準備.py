# coding: utf-8
import os
import json
from requests_oauthlib import OAuth1Session
import requests
import urllib.request
import numpy.random as nmr
import time
import recorder as rc
import gt_v3
import condition_setter as cs

#実行する時間の取得
import datetime as dt
now = dt.datetime.now()
"""
下を0から9に直しておくこと
"""
japan = now + dt.timedelta(hours=0) #Herokuでは時間帯がUTCなので9時間後にずらす
j_hour = japan.hour
if 0 <= j_hour <= 12: am_pm = 0
else: am_pm = 1
"""
#Herokuの環境変数
AT = os.environ["ACCESS_TOKEN"]           # Access Token
AS = os.environ["ACCESS_TOKEN_SECRET"]    # Accesss Token Secert
CK = os.environ["CONSUMER_KEY"]           # Consumer Key
CS = os.environ["CONSUMER_SECRET"]        # Consumer Secret
"""
#予報するアイドルの番号の決定（被りが発生しないようにする）
l_idl_num = nmr.randint(0,11,4)
while l_idl_num[0] == l_idl_num[1]:
    l_idl_num[1] = nmr.randint(7)
while l_idl_num[2] in l_idl_num[:2]:
    l_idl_num[2] =  nmr.randint(7)
while l_idl_num[3] in l_idl_num[:3]:
    l_idl_num[3] =  nmr.randint(7)

#ループの作成
place_box = ["仙台","東京","大阪","福岡"]
for i in range(4):
    if i == 0:
        gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/04.xml",'東部',place_box[i])
    elif i == 1:
        gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',place_box[i])
    elif i == 2:
        gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/27.xml",'大阪府',place_box[i])
    elif i == 3:
        gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/40.xml",'福岡地方',place_box[i])

    data_base = []
    for j in range(7):
        previous = japan - dt.timedelta(days=j+1-am_pm)
        #pre_array = [pre.year,pre.month,pre.day,pre.hour,pre.minute]
        rcd = rc.Recorder(place_box[i],previous)
        rcd.get_info()
        rcd.add_to_excel()
        rcd.eroor_check()
        data_base.append(rcd.get_data(previous))

    #夜の時点では当日の天気情報がないので、予報値を用いる
    if am_pm == 1:
        data_base[0]["day"] = japan.day
        data_base[0]["気温"]["最高"] = float(gt.gt_box_array[0][4][0])
        data_base[0]["気温"]["最低"] = float(gt.gt_box_array[0][4][1])
        data_base[0]["天気概況"]["昼"] = gt.gt_box_array[0][2]

    setter = cs.Setter(am_pm,data_base,gt.gt_box_array[am_pm])


    #print(place_box[i])
    #for z in range(len(data_base)):
    #    print(z)
    #    print(data_base[z])
    #    print("#"*40)

    #print("時刻",j_hour)
    #print("x_num",am_pm)

    idl_num = l_idl_num[i]
    if idl_num == 0:
        import udsuki_v3
        girl = udsuki_v3.Udsuki(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = girl.f_text
        if "海" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'udsuki04{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,32)
            idl_photo = 'udsuki0{}.jpg'.format(p_num)

    elif idl_num == 1:
        import rin_v3
        rin = rin_v3.Rin(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = rin.f_text
        if "海" in tweeting_text:
            idl_photo = 'rin041.jpg'
        else:
            p_num = nmr.randint(1,32)
            idl_photo = 'rin0{}.jpg'.format(p_num)

    elif idl_num == 2:
        import mio_v3
        mio = mio_v3.Mio(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = mio.f_text
        p_num = nmr.randint(1,10)
        idl_photo = 'mio0{}.jpg'.format(p_num)

    elif idl_num == 3:
        import anzu_v3
        anzu = anzu_v3.Anzu(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = anzu.f_text
        p_num = nmr.randint(1,36)
        idl_photo = 'anzu0{}.jpg'.format(p_num)

    elif idl_num == 4:
        import anastasia_v3
        anastasia = anastasia_v3.Anastasia(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = anastasia.f_text
        p_num = nmr.randint(1,13)
        idl_photo = 'anastasia0{}.jpg'.format(p_num)

    elif idl_num == 5:
        import yuko_v3
        yuko = yuko_v3.Yuko(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = yuko.f_text
        if "温泉" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'yuko2{}.jpg'.format(p_num)
        elif "ビーム" in tweeting_text: idl_photo = 'yuko010.jpg'
        else:
            p_num = nmr.randint(1,11)
            idl_photo = 'yuko0{}.jpg'.format(p_num)

    elif idl_num == 6:
        import miku_v3
        miku = miku_v3.Miku(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = miku.f_text
        if "魚" in tweeting_text:
            idl_photo = "miku041.jpg"
        else:
            p_num = nmr.randint(1,38)
            idl_photo = 'miku0{}.jpg'.format(p_num)

    elif idl_num == 7:
        import yoshino_v3
        yoshino = yoshino_v3.Yoshino(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = yoshino.f_text
        if "桜" or "紗枝" in tweeting_text:
            p_num = nmr.randint(1,3)
            idl_photo = 'yoshino3{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,25)
            idl_photo = 'yoshino{}.jpg'.format(p_num)

    elif idl_num == 8:
        import arisu_v3
        arisu = arisu_v2.Arisu(gt.gt_box_array[x_num],x_num,data_base)
        tweeting_text = arisu.f_text
        if "イチゴ" or "いちご" in tweeting_text:
            p_num = nmr.randint(1,6)
            idl_photo = 'arisu_str{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,24)
            idl_photo = 'arisu{}.jpg'.format(p_num)

    elif idl_num == 9:
        import momoka_v3
        momoka = momoka_v3.Momoka(gt.gt_box_array[x_num],x_num,data_base)
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
        import fumika_v3
        fumika = fumika_v3.Fumika(gt.gt_box_array[x_num],x_num,data_base)
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
    time.sleep(10)

"""
gentle-crag-58603　の　tweet03.py を動かす時
heroku run python tweet03.py --app gentle-crag-58603
"""
