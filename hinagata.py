#!/usr/bin/env python
# coding: utf-8

import json
from requests_oauthlib import OAuth1Session

AT = "863556291729301504-MaPF7pwhLQtFwUrtMIzxS0gQd7wEEOC"
AS = "fCp80ufrYK6rMVI9lqC0SOiXE6kRlTj4T7lhw6aZdKDw1"
CK = "fSMitUng7w3UkXU4kCMYrXmC6"
CS = "SSsyuo4tE6RW8yQLAZJLLa9795NYcd4mppLnkEDHOcv6iuSIqU"


url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# OAuth認証 セッションを開始
twitter = OAuth1Session(CK, CS, AT, AS)

# 画像投稿
files = {"media" : open('chieri.jpg', 'rb')}
req_media = twitter.post(url_media, files = files)

# レスポンスを確認
if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

# Media ID を取得
media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

# Media ID を付加してテキストを投稿
params = {'status': 'おはようございます！', "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

# 再びレスポンスを確認
if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")
