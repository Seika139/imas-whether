#encoding:utf-8
import get_tenki_tokyo as gt

aisatsu = "みんな、おっはよ〜！本田未央の天気予報の時間だよ☆"
tenki = "今日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度の予報だよ！".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章の辞書
d_text = {}
d_text["snow"] = "今日は雪が降る予報だって！積もったら雪合戦したいなっ☆"
d_text["fine"] = "今日は晴れていい天気になりそうだよ！なんだかいいことが起こりそうー！"
d_text["storm"] = "今日は暴風雨だけど、雨にも負けず！がんばろー！"
d_text["r_123"] = "今日は1日を通じて降水確率が{}％を越えそうだから、出かけるときは傘を忘れずにね！".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
d_text["r_12"] = "今日は午前中の降水確率が{}％、午後は{}％となる見込みだよっ。傘を忘れずに持っていってね！".format(gt.rain[1],gt.rain[2])
d_text["r_23"] = "今日は午後の降水確率が{}％、夜は{}％だから、朝降ってなくても傘を持っていこう！".format(gt.rain[2],gt.rain[3])
d_text["r_3"] = "今日は夜の降水確率が{}％だよ。夕方から雨が降るかもだねっ。帰りが遅い人は傘を忘れずにー。".format(gt.rain[3])
d_text["r_2"] = "今日は午後の降水確率が{}％だよ。出かける人は傘を持って行こう！".format(gt.rain[2])
d_text["nothing"] = "それじゃあみんな、行ってらっしゃ〜い！"
d_text["under10"] = "今日も寒いけど、元気出していってみよ〜！"
d_text["over30"] = "暑すぎて倒れそう〜。こまめに水分を摂って熱中症対策だね☆"

#雪が降る場合
if "雪" in gt.weather and "雨か雪" not in gt.weather: c_text = d_text["snow"]
#ただの「晴れ」の場合
elif "100" in gt.weather_id: c_text = d_text["fine"]
#強い雨が降る場合
elif "307" in gt.weather_id or "308" in gt.weather_id: c_text = d_text["storm"]
#雷の恐れがある場合

#降水確率のチェック
elif "雨" in gt.weather or min(gt.rain) >= 10:
    if min(gt.rain[1],gt.rain[2],gt.rain[3]) >= 30:
        c_text = d_text["r_123"]        #1日を通して降水確率が30%以上
    elif min(gt.rain[1],gt.rain[2]) >= 30:
        c_text = d_text["r_12"]      #午前と午後の降水確率が30%以上
    elif min(gt.rain[2],gt.rain[3]) >= 30:
        c_text = d_text["r_23"]     #午後と夜の降水確率が30%以上
    elif gt.rain[3] >= 30:
        c_text = d_text["r_3"]      #夜の降水確率が30%以上
    elif gt.rain[2] >= 30:
        c_text = d_text["r_2"]      #午後の降水確率が30%以上
    else:
        c_text = d_text["nothing"]      #それ以外

#気温が低いとき
elif int(gt.kion_box[0]) <= 10: c_text = d_text["under10"]

#気温が高いとき
elif int(gt.kion_box[0]) >= 30: c_text = d_text["over30"]

#どの条件にも一致しなかった場合
else: c_text = d_text["nothing"]


#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"
print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("#"*60)
    print("このモジュールは本田未央の「デレマス朝の天気予報」をお伝えします。")
    print("文字数のチェックを実施します。")
    print("="*60)
    print(aisatsu,":",len(aisatsu),"words")
    print(tenki+kion,":",len(tenki+kion),"words")
    print("残り文字数",140-len(aisatsu)-len(tenki+kion)-11,"words")
    for i in d_text:
        print("-"*60)
        print(i,":",d_text[i],":",len(d_text[i]),"words")
    print("-"*60)
