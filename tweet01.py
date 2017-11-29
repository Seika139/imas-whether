# coding:utf-8
import twitter

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""


auth = twitter.OAuth(consumer_key="863556291729301504-MaPF7pwhLQtFwUrtMIzxS0gQd7wEEOC",
consumer_secret="fCp80ufrYK6rMVI9lqC0SOiXE6kRlTj4T7lhw6aZdKDw1",
token="fSMitUng7w3UkXU4kCMYrXmC6",
token_secret="SSsyuo4tE6RW8yQLAZJLLa9795NYcd4mppLnkEDHOcv6iuSIqU")

t = twitter.Twitter(auth=auth)

#ツイートのみ
status="外人ぽい人が自販機の前で「この中のどのコーヒーが甘いですか」と聞かれたが、そんなこと聞かれても..." #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

#画像付きツイート
pic=""　#画像を投稿するなら画像のパス
with open(pic,"rb") as image_file:
 image_data=image_file.read()
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
t.statuses.update(status=status,media_ids=",".join([id=img1]))
