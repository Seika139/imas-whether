# coding:utf-8
from numpy.random import *
import twitter
import os


consumer_key = os.environ["CONSUMER_KEY"],
consumer_secret = os.environ["CONSUMER_SECRET"],
token = os.environ["ACCESS_TOKEN"],
token_secret = os.environ["ACCESS_TOKEN_SECRET"]

t = twitter.Twitter(auth = OAuth(token,token_secret,consumer_key,consumer_secret))

#ツイートのみ
status="外人ぽい人が自販機の前で「この中のどのコーヒーが甘いですか?」と聞かれたが、そんなこと聞かれても..." #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

#画像付きツイート
pic="udsuki2.jpg" #画像を投稿するなら画像のパス
with open(pic,"rb") as image_file:
    image_data=image_file.read()
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
t.statuses.update(status=status,media_ids=",".join([id_img1]))




"""
-----> PHP app detected
 !     WARNING: No 'composer.json' found.
       Using 'index.php' to declare app type as PHP is considered legacy
       functionality and may lead to unexpected behavior.
-----> Bootstrapping...
-----> Installing platform packages...
       NOTICE: No runtime required in composer.lock; using PHP ^5.5.17
       - php (5.6.32)
       - apache (2.4.29)
       - nginx (1.8.1)
-----> Installing dependencies...
       Composer version 1.5.2 2017-09-11 16:59:25
-----> Preparing runtime environment...
-----> Checking for additional extensions to install...
-----> Python app detected
-----> Installing requirements with pip
-----> Discovering process types
       Procfile declares types -> web
-----> Compressing...
       Done: 76.3M
-----> Launching...


"""
