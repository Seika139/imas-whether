# -*- coding: utf-8 -*-

from datetime import *
import twitter
import os


now = datetime.today() - timedelta(0,60)
text =  str(now.year) + u"年" + str(now.month) + u"月" + str(now.day) + u"日" + str(now.hour) + u"時" + str(now.minute) + u"分のTwitterトレンドです。"

#print text


token = "863556291729301504-MaPF7pwhLQtFwUrtMIzxS0gQd7wEEOC"
token_secret = "fCp80ufrYK6rMVI9lqC0SOiXE6kRlTj4T7lhw6aZdKDw1"
consumer_key = "fSMitUng7w3UkXU4kCMYrXmC6"
consumer_secret = "SSsyuo4tE6RW8yQLAZJLLa9795NYcd4mppLnkEDHOcv6iuSIqU"

auth = twitter.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(token,token_secret)

api = twitter.API(auth)

api.update_with_media(filename='./now.png',status=text)
