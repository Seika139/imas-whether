#encoding:utf-8
import get_tenki as gt
import numpy.random as nmr


#挨拶の文章
def aisatsu():
    num = nmr.randint(2)
    if num == 0:
        aisatsu = "ドーブラエ ウートラ！おはようございます。アーニャが天気予報をお伝えしますね。"
    elif num == 1 :
        aisatsu = "プラグノス　パゴーダ…今日の天気予報はアーニャの番ですよ。"
    return aisatsu

aisatsu = aisatsu()
tenki = "今日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度です。".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章
c_text = ""

#何もない時の文章
def nothing():
    num = nmr.randint(3)
    if num == 0:
        c_text = "ダー。天気予報…日本語の練習になりますね。"
    elif num == 1:
        c_text = "アーニャはズヴェズダ…星を眺めるのが好きですが、昼間の空も綺麗ですね。"
    elif num == 2:
        c_text = "空の表情はとても豊かですね。アーニャもそんな風になりたいです。"
    return c_text

#雪が降る場合
if "雪" in gt.weather and "雨か雪" not in gt.weather:
    c_text = "スニェーク…。雪は冷たいけど、心は温まりますね。"

#ただの「晴れ」の場合
elif "100" in gt.weather_id:
    c_text = "今日は気持ちのよい日、になりそうです。"

#強い雨が降る場合
elif "307" in gt.weather_id or "308" in gt.weather_id:
    c_text = "雨も風も強いです。ロシアのミチェーリ…吹雪みたいです。気をつけてくださいね。"

#雷の恐れがある場合


#降水確率のチェック
elif "雨" in gt.weather or min(gt.rain) >= 10:
    if min(gt.rain[1],gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は一日中降水確率が{}％を越えますね。ゾーンチク…傘を持っていきましょう。".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
    elif min(gt.rain[1],gt.rain[2]) >= 30:
        c_text = "午前中の降水確率が{}％、午後は{}％です。ゾーンチク…傘を持って出かけましょう。".format(gt.rain[1],gt.rain[2])
    elif min(gt.rain[2],gt.rain[3]) >= 30:
        c_text = "午後の降水確率が{}％、夜は{}％です。ゾーンチク…傘を持って出かけましょう。".format(gt.rain[2],gt.rain[3])
    elif gt.rain[3] >= 30:
        c_text = "今日は夜の降水確率が{}％。夕方から雨が降りそうですよ。".format(gt.rain[3])
    elif gt.rain[2] >= 30:
        c_text = "今日は午後の降水確率が{}％です。ゾーンチク…傘を持っていきましょう。".format(gt.rain[2])
    else: c_text = nothing()

#気温が低いとき
elif int(gt.kion_box[1]) <= 0:
    num = nmr.randint(2)
    if num == 0:
        c_text = "ロシアほどじゃないですが、日本も寒いですね。"
    elif num == 1:
        c_text = "これだけ寒いと、池が凍りますね。"

#気温が高いとき
elif int(gt.kion_box[0]) >= 30:
    num = nmr.randint(2)
    if num == 0:
        c_text = "ダー。日本の夏はジメジメ？してます。熱中症に気をつけてくださいね。"
    elif num == 1:
        c_text =  "アーニャ暑いの苦手です…いっぱいお水を飲みましょう。"

#どの条件にも一致しなかった場合
else: c_text = nothing()


#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"
print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("このモジュールはアナスタシアの「デレマス朝の天気予報」をお伝えします。")
