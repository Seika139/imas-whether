#encoding:utf-8

import gt_v2 as p_gt
import mio_v2 as p_mio

gt = p_gt.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',"東京")
mio = p_mio.Mio(gt.gt_box_array[0])
print("*"*10)
print(mio.f_text)


import datetime as dt
xd = dt.datetime.today()
xh = xd.hour
print(xh)
if xh >= 0 and xh <= 12:
    print("朝")
else:
    print("夜")


"""
gt_v2　は完成
mio_v2　は朝と夜に応じた文章とそのシステムづくり
tweet_v2 も同じ


"""
