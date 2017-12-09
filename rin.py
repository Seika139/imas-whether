#encoding:utf-8
import get_tenki as gt

aisatsu = "みんなおはよう…渋谷凛です。\
今日の天気予報をお知らせします。"
tenki = "今日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度の予報です。".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章
c_text = ""

#雪が降る場合
if "雪" in gt.weather and "雨か雪" not in gt.weather:
    c_text = "今日は雪が降る予報だよ。\
交通機関が遅延するかもだから、そっちも…チェックしてみてね。"

#ただの「晴れ」の場合
elif "100" in gt.weather_id:
    c_text = "今日はとてもいい天気になりそう…\n\
こんな日にライブしたいなぁ…なんてね。"

#強い雨が降る場合
elif "307" in gt.weather_id or "308" in gt.weather_id:
    c_text = "今日は雨も風も強いみたい…\
出かけるときは気をつけてね。"

#雷の恐れがある場合


#降水確率のチェック
else:
    if min(gt.rain[1],gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は1日を通じて降水確率が{}％を越えそうだから、出かけるときは\
傘を忘れずにね。".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
    elif min(gt.rain[1],gt.rain[2]) >= 30:
        c_text = "今日は午前中の降水確率が{}％、午後は{}％となる見込みだよ。\
傘を忘れずに持っていってね。".format(gt.rain[1],gt.rain[2])
    elif min(gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は午後の降水確率が{}％、夜は{}％だから、雨が降って\
なくても、傘を持っていくといいかもね。".format(gt.rain[2],gt.rain[3])
    elif gt.rain[3] >= 30:
        c_text = "今日は夜の降水確率が{}％。夕方から雨が降りそうだよ…\
帰りが遅い人は傘を忘れずにね。".format(gt.rain[3])
    elif gt.rain[2] >= 30:
        c_text = "今日は午後の降水確率が{}％だよ。傘…\
持って行ってね。".format(gt.rain[2])

    #どの条件にも一致しなかった場合
    else:
        c_text = "以上、天気予報でした…"



#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"
print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("このモジュールは渋谷凛の「デレマス朝の天気予報」をお伝えします。")
