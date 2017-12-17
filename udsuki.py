#encoding:utf-8
import get_tenki as gt

aisatsu = "皆さんおはようございます！島村卯月の「デレマス朝の天気予報」のコーナーです。"
tenki = "本日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度です。".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章
c_text = ""

#雪が降る場合
if "雪" in gt.weather and "雨か雪" not in gt.weather:
    c_text = "今日は雪が降る予報になっています。交通機関の情報にも注意して出かけてくださいね！"

#ただの「晴れ」の場合
elif "100" in gt.weather_id:
    c_text = "今日はよく晴れたいい天気になりそうで、私も頑張れそうです！\n皆さんも良い1日を〜♪"

#強い雨が降る場合
elif "307" in gt.weather_id or "308" in gt.weather_id:
    c_text = "今日は強い雨と風が吹き荒れるようです。出かける際は十分に気をつけてくださいね！"

#雷の恐れがある場合


#降水確率のチェック
elif "雨" in gt.weather or min(gt.rain) >= 10:
    if min(gt.rain[1],gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は1日を通じて降水確率が{}％を越えそうです。出かけるときは傘を忘れずに持っていきましょう".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
    elif min(gt.rain[1],gt.rain[2]) >= 30:
        c_text = "今日は午前中の降水確率が{}％、午後は{}％となる見込みです。傘を忘れずに持っていきましょう。".format(gt.rain[1],gt.rain[2])
    elif min(gt.rain[2],gt.rain[3]) >= 30:
        c_text = "今日は午後の降水確率が{}％、夜は{}％となっています。朝は雨が降っていなくても、傘を持っていくといいでしょう。".format(gt.rain[2],gt.rain[3])
    elif gt.rain[3] >= 30:
        c_text = "今日は夜の降水確率が{}％となっていて、夕方から雨が降りそうです。帰りが遅い人は傘を持っていくといいでしょう。".format(gt.rain[3])
    elif gt.rain[2] >= 30:
        c_text = "今日は午後の降水確率が{}％となっています。傘があると良いでしょう。".format(gt.rain[2])
    else: c_text = "それでは、今日も一日頑張っていきましょう！"

#気温が低いとき
elif int(gt.kion_box[0]) <= 10:
    c_text = "冷え込むので、暖かい格好をして出かけましょう！"

#気温が高いとき
elif int(gt.kion_box[0]) >= 30:
    c_text = "暑いので熱中症には気をつけてくださいね!"

#どの条件にも一致しなかった場合
else: c_text = "それでは、今日も一日頑張っていきましょう！"



#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"

print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("このモジュールは島村卯月の「デレマス朝の天気予報」をお伝えします。")
