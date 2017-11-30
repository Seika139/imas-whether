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
環境変数を参照する時
heroku config --app gentle-crag-58603

gentle-crag-58603　の　tweet01.py を動かす時
heroku run python tweet01.py --app gentle-crag-58603
"""
