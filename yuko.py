#encoding:utf-8
import get_tenki as gt
import numpy.random as nmr


#挨拶の文章
def aisatsu():
    num = nmr.randint(2)
    if num == 0:
        aisatsu = "みなさん、おはようございます！エスパーユッコこと、堀裕子のさいきっく天気予報の時間です！"
    elif num == 1 :
        aisatsu = "むむむーんっ、今からユッコのさいきっくぱわーで天気を予知しちゃいますよ！"
    return aisatsu

aisatsu = aisatsu()
tenki = "今日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度です。".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章
c_text = ""

#何もない時の文章
def nothing():
    num = nmr.randint(2)
    if num == 0:
        c_text = "twitterだけでなくテレパシーでも届けちゃいますよ。ムムムーン！"
    elif num == 1:
        c_text = "次はユッコの特技、スプーン曲げを披露しちゃいますよ…え、時間がない！？"
    return c_text

#雪が降る場合
if "雪" in gt.weather and "雨か雪" not in gt.weather:
    c_text = "雪が積もったら、さいきっく雪合戦です！"

#ただの「晴れ」の場合
elif "100" in gt.weather_id:
    c_text = "今日はいい天気ですね！さいきっくぱわーを磨くにはもってこいです！"

#強い雨が降る場合
elif "307" in gt.weather_id or "308" in gt.weather_id:
    c_text = "今日は嵐です…流石の私でも、さいきっくぱわーで天気を変えることはできません…"

#雷の恐れがある場合


#降水確率のチェック
elif "雨" in gt.weather or min(gt.rain) >= 10:
    if min(gt.rain[1],gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は一日を通して降水確率が{}％を越えそうなので傘が必要ですよ！".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
    elif min(gt.rain[1],gt.rain[2]) >= 30:
        c_text = "今日は午前中の降水確率が{}％、午後は{}％です。傘を持って出かけましょう！".format(gt.rain[1],gt.rain[2])
    elif min(gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は午後の降水確率が{}％、夜は{}％だから、雨が降ってなくても傘を持っていきましょう！".format(gt.rain[2],gt.rain[3])
    elif gt.rain[3] >= 30:
        c_text = "今日は夜の降水確率が{}％です。出かける時は傘を持っていきましょう！".format(gt.rain[3])
    elif gt.rain[2] >= 30:
        c_text = "今日は午後の降水確率が{}％です。出かける時は傘を持っていきましょう！".format(gt.rain[2])
    else: c_text = nothing()

#気温が低いとき
elif int(gt.kion_box[0]) <= 10:
    c_text = "こんな寒い日は温泉に浸かってエナジーを蓄えましょう！"

#気温が高いとき
elif int(gt.kion_box[0]) >= 30:
    c_text = "私のスプーン、アイスを食べる時も使えるんですよ。便利でしょう！"
#どの条件にも一致しなかった場合
else: c_text = nothing()


#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"
print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("このモジュールは堀裕子の「デレマス朝の天気予報」をお伝えします。")
