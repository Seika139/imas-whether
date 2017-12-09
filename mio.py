#encoding:utf-8
import get_tenki as gt

aisatsu = "みんな、おっはよ〜！本田未央の天気予報の時間だよ☆"
tenki = "今日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度の予報だよ！".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章
c_text = ""

#雪が降る場合
if "雪" in gt.weather and "雨か雪" not in gt.weather:
    c_text = "今日は雪が降る予報だって！積もったら雪合戦したいなっ☆"

#ただの「晴れ」の場合
elif "100" in gt.weather_id:
    c_text = "今日は晴れていい天気になりそうだよ！なんだかいいことが起こりそうー！"

#強い雨が降る場合
elif "307" in gt.weather_id or "308" in gt.weather_id:
    c_text = "今日は暴風雨だけど、雨にも負けず！がんばろー！"

#雷の恐れがある場合


#降水確率のチェック
elif "雨" in gt.weather or min(gt.rain) >= 10:
    if min(gt.rain[1],gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は1日を通じて降水確率が{}％を越えそうだから、出かけるときは\
傘を忘れずにね！".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
    elif min(gt.rain[1],gt.rain[2]) >= 30:
        c_text = "今日は午前中の降水確率が{}％、午後は{}％となる見込みだよっ。\
傘を忘れずに持っていってね！".format(gt.rain[1],gt.rain[2])
    elif min(gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は午後の降水確率が{}％、夜は{}％だから、朝降って\
なくても傘を持っていこう！".format(gt.rain[2],gt.rain[3])
    elif gt.rain[3] >= 30:
        c_text = "今日は夜の降水確率が{}％だよ。夕方から雨が降るかもだねっ。\
帰りが遅い人は傘を忘れずにー。".format(gt.rain[3])
    elif gt.rain[2] >= 30:
        c_text = "今日は午後の降水確率が{}％だよ。出かける人は傘を持って行こう！".format(gt.rain[2])
    else: c_text = "それじゃあみんな、行ってらっしゃ〜い！"


#気温が低いとき
elif int(gt.kion_box[0]) <= 10:
    c_text = "今日も寒いけど、元気出して行ってみよ〜！"

#気温が高いとき
elif int(gt.kionbox[0]) >= 30:
    c_text = "暑すぎて倒れそう〜。こまめに水分を摂って熱中症対策だ☆"

#どの条件にも一致しなかった場合
else: c_text = "それじゃあみんな、行ってらっしゃ〜い！"


#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"
print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("このモジュールは本田未央の「デレマス朝の天気予報」をお伝えします。")
