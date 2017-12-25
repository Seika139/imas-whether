#encoding:utf-8
import get_tenki2 as gt
import numpy.random as nmr


#挨拶の文章
def aisatsu():
    num = nmr.randint(2)
    if num == 0: aisatsu = "えー今日の天気予報、杏の番なの？？しょーがないな…"
    elif num == 1 : aisatsu = "みんな、だらだらしてる〜？双葉杏の天気予報の時間だよー"
    return aisatsu

aisatsu = aisatsu()
tenki = "今日の{}の天気は「{}」、".format(gt.place,gt.weather)
kion = "最高気温は{}度、最低気温は{}度でーす。".format(gt.kion_box[0],gt.kion_box[1])

#最後の天気によっって変化する文章の辞書
d_text = {}
d_text["nothing1"] = "はい、天気予報頑張ったから、飴くれ！"
d_text["nothing2"] = "じゃあ事務所に帰ってもうひと眠りするか…え、だめ！？"
d_text["nothing3"] = "今日もゆる〜く行こうよ…ね♪"
d_text["snow"] = "雪が降るんならお家でぬくぬく過ごしたいなぁ〜"
d_text["fine"] = "今日はとってもいい天気！お昼寝日和だぁ〜"
d_text["storm"] = "今日は雨も風も強いし、仕事なんかしてる場合じゃない！杏を帰らせろー！"
d_text["r_123"] = "今日は一日中降水確率が{}％を越えそうだから傘が必要だよ。".format(min(gt.rain[1],gt.rain[2],gt.rain[3]))
d_text["r_12"] = "今日は午前中の降水確率が{}％、午後は{}％だって…傘を忘れずに持っていってね♪".format(gt.rain[1],gt.rain[2])
d_text["r_23"] = "午後の降水確率が{}％、夜は{}％だから、雨が降ってなくても、傘を持っていこう！".format(gt.rain[2],gt.rain[3])
d_text["r_3"] = "今日は夜の降水確率が{}％。夕方から雨が降りそうだから杏は早くかーえろっと。".format(gt.rain[3])
d_text["r_2"] = "今日は午後の降水確率が{}％だよ。傘を持っていくといいよ〜".format(gt.rain[2])
d_text["under10-1"] = "こんな寒い日はこたつの中でゴロゴロするのが１番！"
d_text["under10-2"] = "みんな、風邪ひかないようにね〜"
d_text["over30-1"] = "あつーい、エアコンの効いた部屋から出られないよ。"
d_text["over30-2"] = "今日は飴じゃなくてアイスが食べたいな〜"

#何もない時の文章
def nothing():
    num = nmr.randint(3)
    if num == 0: c_text = d_text["nothing1"]
    elif num == 1: c_text = d_text["nothing2"]
    elif num == 2: c_text = d_text["nothing3"]
    return c_text

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
        c_text = nothing()      #それ以外

#気温が低いとき
elif int(gt.kion_box[0]) <= 10:
    num = nmr.randint(2)
    if num == 0: c_text = d_text["under10-1"]
    elif num == 1: c_text = d_text["under10-2"]

#気温が高いとき
elif int(gt.kion_box[0]) >= 30:
    num = nmr.randint(2)
    if num == 0: c_text = d_text["over30-1"]
    elif num == 1: c_text =  d_text["over30-2"]

#どの条件にも一致しなかった場合
else: c_text = nothing()


#最終的な文章の合成
f_text = aisatsu+"\n"+tenki+kion+"\n"+c_text+"\n"+"#デレマス朝の天気予報"
print(f_text)
print(len(f_text),"words")


if __name__ == "__main__":
    print("#"*60)
    print("このモジュールは双葉杏の「デレマス朝の天気予報」をお伝えします。")
    print("文字数のチェックを実施します。")
    print("="*60)
    print(aisatsu,":",len(aisatsu),"words")
    print(tenki+kion,":",len(tenki+kion),"words")
    print("残り文字数",140-len(aisatsu)-len(tenki+kion)-11,"words")
    for i in d_text:
        print("-"*60)
        print(i,":",d_text[i],":",len(d_text[i]),"words")
    print("-"*60)
