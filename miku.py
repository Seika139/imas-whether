#encoding:utf-8
import get_tenki as gt
import numpy.random as nmr


#挨拶の文章
def aisatsu():
    num = nmr.randint(2)
    if num == 0:
        aisatsu = "えー今日の天気予報、杏の番なの？？\nしょーがないな…"
    elif num == 1 :
        aisatsu = "みんな、おはよ〜！みくのにゃんにゃん天気予報始まるよー"
    return aisatsu

aisatsu = aisatsu()
tenki = "今日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度だにゃ！".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章
c_text = ""

#何もない時の文章
def nothing():
    num = nmr.randint(3)
    if num == 0:
        c_text = "はい、天気予報頑張ったから、飴くれ！"
    elif num == 1:
        c_text = "じゃあ事務所に帰ってもうひと眠りするか…え、だめ！？"
    elif num == 2:
        c_text = "今日もゆる〜く行こうよ…ね♪"
    return c_text

#雪が降る場合
if "雪" in gt.weather and "雨か雪" not in gt.weather:
    c_text = "雪が降るんならお家でぬくぬく過ごしたいなぁ〜"

#ただの「晴れ」の場合
elif "100" in gt.weather_id:
    c_text = "今日はとってもいい天気！お昼寝日和だぁ〜"

#強い雨が降る場合
elif "307" in gt.weather_id or "308" in gt.weather_id:
    c_text = "今日は雨も風も強いし、仕事なんかしてる場合じゃない！杏を帰らせろー！"

#雷の恐れがある場合


#降水確率のチェック
elif "雨" in gt.weather or min(gt.rain) >= 10:
    if min(gt.rain[1],gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は一日中降水確率が{}％を越えそうだから傘が必要だよ。".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
    elif min(gt.rain[1],gt.rain[2]) >= 30:
        c_text = "今日は午前中の降水確率が{}％、午後は{}％だって…傘を忘れずに持っていってね♪".format(gt.rain[1],gt.rain[2])
    elif min(gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は午後の降水確率が{}％、夜は{}％だから、雨が降ってなくても、傘を持っていこう！".format(gt.rain[2],gt.rain[3])
    elif gt.rain[3] >= 30:
        c_text = "今日は夜の降水確率が{}％。夕方から雨が降りそうだから杏は早くかーえろっと。".format(gt.rain[3])
    elif gt.rain[2] >= 30:
        c_text = "今日は午後の降水確率が{}％だよ。傘を持っていくといいよ〜".format(gt.rain[2])
    else: c_text = nothing()

#気温が低いとき
elif int(gt.kion_box[0]) <= 10:
    num = nmr.randint(2)
    if num == 0:
        c_text = "こんな寒い日はこたつの中でゴロゴロするのが１番！"
    elif num == 1:
        c_text = "みんな、風邪ひかないようにね〜"

#気温が高いとき
elif int(gt.kion_box[0]) >= 30:
    num = nmr.randint(2)
    if num == 0:
        c_text = "あつーい、エアコンの効いた部屋から出られないよ。"
    elif num == 1:
        c_text =  "今日は飴じゃなくてアイスが食べたいな〜"

#どの条件にも一致しなかった場合
else: c_text = nothing()


#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"
print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("このモジュールは前川みくの「デレマス朝の天気予報」をお伝えします。")
