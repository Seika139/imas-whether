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
"""
下の2番目の数字を変える
"""
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
    if i == 0:    gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/04.xml",'東部',place_box[i])
    elif i == 1:  gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',place_box[i])
    elif i == 2:  gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/27.xml",'大阪府',place_box[i])
    elif i == 3:  gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/40.xml",'福岡地方',place_box[i])

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

    idl_num = l_idl_num[i]
    if idl_num == 0:
        import udsuki_v3
        udsuki = udsuki_v3.Udsuki(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = udsuki.f_text
        if japan.month==1 and japan.day<=4:  idl_photo = 'udsuki0{}.jpg'.format(nmr.randint(9,11))
        if japan.month==2 and japan.day==14: idl_photo = 'udsuki02.jpg'
        if '桜' in tweeting_text or '花見' in tweeting_text:  idl_photo = 'udsuki0{}.jpg'.format(nmr.randint(35,37))
        if "スクール水着" in tweeting_text:  idl_photo = "udsuki033.jpg"
        if "海" in tweeting_text:  idl_photo = 'udsuki034.jpg'
        else:  idl_photo = 'udsuki0{}.jpg'.format(nmr.randint(1,37))

    elif idl_num == 1:
        import rin_v3
        rin = rin_v3.Rin(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = rin.f_text
        if "海" in tweeting_text:    idl_photo = 'rin028.jpg'
        elif japan.month==1 and japan.day<=4:  idl_photo = 'rin0{}.jpg'.format(nmr.randint(35,38))
        elif japan.month==2 and japan.day==14:  idl_photo = 'rin0{}.jpg'.format(nmr.randint(31,35))
        else:  idl_photo = 'rin0{}.jpg'.format(nmr.randint(1,38))

    elif idl_num == 2:
        import mio_v3
        mio = mio_v3.Mio(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = mio.f_text
        if 'カマクラ' in tweeting_text:  idl_photo = 'mio33.jpg'
        elif '水着' in tweeting_text:   idl_photo = 'mio{}.jpg'.format(nmr.randint(24,27))
        elif japan.month==1 and japan.day<=3:  idl_photo = 'mio0{}.jpg'.format(nmr.randint(28,31))
        elif japan.month==9 and 3<=japan.day<=4:  idl_photo = 'mio0{}.jpg'.format(nmr.randint(29,31))
        elif japan.month==11 and 28<=japan.day<=29:  idl_photo = 'mio0{}.jpg'.format(nmr.randint(29,31))
        elif '雪' in tweeting_text　or '真っ白' in tweeting_text:   idl_photo = 'mio{}.jpg'.format(nmr.randint(31,34))
        else:  idl_photo = 'mio0{}.jpg'.format(nmr.randint(1,36))

    elif idl_num == 3:
        import anzu_v3
        anzu = anzu_v3.Anzu(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = anzu.f_text
        if japan.month==12 and 23<japan.day<26: idl_photo = 'anzu013.jpg'
        elif　japan.month==2 and japan.day==14: idl_photo = 'anzu019.jpg'
        elif　'麦わら帽子' in tweeting_text: idl_photo = 'anzu016.jpg'
        elif 'トロピカル' in tweeting_text or '海' in tweeting_text: idl_photo = 'anzu03.jpg'
        else: idl_photo = 'anzu0{}.jpg'.format(nmr.randint(1,40))

    elif idl_num == 4:
        import anastasia_v3
        anastasia = anastasia_v3.Anastasia(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = anastasia.f_text
        idl_photo = 'anastasia{}.jpg'.format(nmr.randint(1,33))

    elif idl_num == 5:
        import yuko_v3
        yuko = yuko_v3.Yuko(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = yuko.f_text
        if 'スイカ' in tweeting_text: idl_photo = 'yuko25.jpg'
        elif "温泉" in tweeting_text: idl_photo = 'yuko{}.jpg'.format(nmr.randint(30,33))
        elif "ビーム" in tweeting_text: idl_photo = 'yuko14.jpg'
        else: idl_photo = 'yuko{}.jpg'.format(nmr.randint(1,33))

    elif idl_num == 6:
        import miku_v3
        miku = miku_v3.Miku(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = miku.f_text
        if "魚" in tweeting_text: idl_photo = "miku0{}.jpg".format(nmr.randint(38,40))
        elif '水着' in tweeting_text: idl_photo = 'miku0{}.jpg'.format(nmr.randint(32,34))
        elif japan.month==2 and japan.day==14: idl_photo = 'miku020.jpg'
        elif japan.month==12 and 24<=japan.day<=25: idl_photo = 'miku015.jpg'
        else: idl_photo = 'miku0{}.jpg'.format(nmr.randint(1,40))

    elif idl_num == 7:
        import yoshino_v3
        yoshino = yoshino_v3.Yoshino(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = yoshino.f_text
        if japan.month==1 and japan.day<=3: idl_photo='yoshino{}.jpg'.format(nmr.randint(12,14))
        elif '温泉' in tweeting_text or '湯' in tweeting_text: idl_photo='yoshino{}.jpg'.format(nmr.randint(19,21))
        elif 'もみじ' in tweeting_text: idl_photo='yoshino{}.jpg'.format(nmr.randint(17,23))
        elif '紅葉' in tweeting_text: idl_photo='yoshino{}.jpg'.format(nmr.randint(17,23))
        elif '木の葉は色づい' in tweeting_text: idl_photo='yoshino{}.jpg'.format(nmr.randint(17,23))
        elif 'かき氷' in tweeting_text: idl_photo = 'yoshino16.jpg'
        elif 'みそぎ' in tweeting_text: idl_photo = 'yoshino14.jpg'
        if "桜" in tweeting_text or "紗枝" in tweeting_text: idl_photo = 'yoshino{}.jpg'.format(nmr.randint(23,27))
        else: idl_photo = 'yoshino{}.jpg'.format(nmr.randint(1,27))

    elif idl_num == 8:
        import arisu_v3
        arisu = arisu_v2.Arisu(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = arisu.f_text
        if "イチゴ" or "いちご" in tweeting_text:
            p_num = nmr.randint(1,6)
            idl_photo = 'arisu_str{}.jpg'.format(p_num)
        else:
            p_num = nmr.randint(1,24)
            idl_photo = 'arisu{}.jpg'.format(p_num)

    elif idl_num == 9:
        import momoka_v3
        momoka = momoka_v3.Momoka(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = momoka.f_text
        if 'シャボン玉' in tweeting_text: idl_photo='momoka26.jpg'
        elif 'お花見' in tweeting_text or 'パリラ' in tweeting_text: idl_photo='momoka35.jpg'
        elif 'まゆさん' in tweeting_text or '杏さん' in tweeting_text: idl_photo='momoka36.jpg'
        elif "夜更かし" in tweeting_text: idl_photo = 'momoka{}.jpg'.format(nmr.randint(33,35))
        elif '仁奈' in tweeting_text: idl_photo='momoka15.jpg'
        elif '線香花火' in tweeting_text: idl_photo='momoka20.jpg'
        elif japan.month==2 and japan.day==14: idl_photo='momoka5.jpg'
        elif japan.month==6 and japan.day==2: idl_photo='momoka{}.jpg'.format(nmr.randint(8,11))
        elif '水' in tweeting_text: idl_photo = 'momoka{}.jpg'.format(nmr.randint(18,20))
        else: idl_photo = 'momoka{}.jpg'.format(nmr.randint(1,37))

    elif idl_num == 10:
        import fumika_v3
        fumika = fumika_v3.Fumika(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = fumika.f_text
        if "ナイトプール" in tweeting_text:
            idl_photo = 'fumika27.jpg'
        else:
            p_num = nmr.randint(1,29)
            idl_photo = 'fumika{}.jpg'.format(p_num)

    elif idl_num == 11:
        import sachiko_v3
        sachiko = sachiko_v3.Sachiko(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
        tweeting_text = sachiko.f_text
        if '水泳のテスト' or '泳げますよ' in tweeting_text: idl_photo = 'sachiko34.jpg'
        elif '小テスト' in tweeting_text: idl_photo = 'sachiko13.jpg'
        else: idl_photo = 'sachiko{}.jpg'.format(nmr.randint(1,35))


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
