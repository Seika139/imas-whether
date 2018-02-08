#encoding:utf-8
class Mio:
    def __init__(self,box,time):

        self.place = box[0]
        self.reporting_date = box[1]
        self.weather = box[2]
        self.weather_id = box[3]
        self.kion_box = box[4]
        self.jikantai = box[5]
        self.rain = box[6]
        self.time = time

        if self.time == 0:
            self.x_date = "今日"
            self.aisatsu = "みんな、おっはよ〜！本田未央の天気予報の時間だよ☆"
        else:
            self.x_date = "明日"
            self.aisatsu = "こんばんは、本田未央だよ☆ みんなに明日の天気を教えてあげよう！"

        self.tenki = "{}の{}の天気は「{}」、".format(self.x_date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報だよ！".format(self.kion_box[0],self.kion_box[1])

        #最後の天気によっって変化する文章の辞書
        self.d_text = {}
        self.d_text["snow"] = "{}は雪が降る予報だって！積もったら雪合戦したいなっ☆".format(self.x_date)
        self.d_text["fine"] = "{}は晴れていい天気になりそうだよ！なんだかいいことが起こりそうー！".format(self.x_date)
        self.d_text["storm"] = "{}は暴風雨だけど、雨にも負けず！がんばろー！".format(self.x_date)
        self.d_text["r_123"] = "{}は1日を通じて降水確率が{}％を越えそうだから、出かけるときは傘を忘れずにね！".format(self.x_date,min(self.rain[1],self.rain[2],self.rain[3]))
        self.d_text["r_12"] = "{}は午前中の降水確率が{}％、午後は{}％となる見込みだよっ。傘を忘れずに持っていってね！".format(self.x_date,self.rain[1],self.rain[2])
        self.d_text["r_23"] = "{}は午後の降水確率が{}％、夜は{}％だから、朝降ってなくても傘を持っていこう！".format(self.x_date,self.rain[2],self.rain[3])
        self.d_text["r_3"] = "{}は夜の降水確率が{}％だよ。夕方から雨が降るかもだねっ。帰りが遅い人は傘を忘れずにー。".format(self.x_date,self.rain[3])
        self.d_text["r_2"] = "{}は午後の降水確率が{}％だよ。出かける人は傘を持って行こう！".format(self.x_date,self.rain[2])
        if self.time == 0: self.d_text["nothing"] = "それじゃあみんな、行ってらっしゃ〜い！"
        else: self.d_text["nothing"] = "それじゃあみんな、おやすみなさ〜い"
        self.d_text["under10"] = "{}も寒いけど、元気出していってみよ〜！".format(self.x_date)
        self.d_text["over30"] = "暑すぎて倒れそう〜。こまめに水分を摂って熱中症対策だね☆"
        self.d_text["kionsa"] = "{}は気温差が激しいよ。脱ぎ着のしやすい服がいいかもね☆".format(self.x_date)


        #雪が降る場合
        if "雪" in self.weather and "雨か雪" not in self.weather:
            self.c_text = self.d_text["snow"]
        #ただの「晴れ」の場合
        elif "100" in self.weather_id:
            self.c_text = self.d_text["fine"]
        #強い雨が降る場合
        elif "307" in self.weather_id or "308" in self.weather_id:
            self.c_text = self.d_text["storm"]
        #雷の恐れがある場合

        #降水確率のチェック
        elif "雨" in self.weather or min(self.rain) >= 10:
            if min(self.rain[1],self.rain[2],self.rain[3]) >= 30:
                self.c_text = self.d_text["r_123"]        #1日を通して降水確率が30%以上
            elif min(self.rain[1],self.rain[2]) >= 30:
                self.c_text = self.d_text["r_12"]      #午前と午後の降水確率が30%以上
            elif min(self.rain[2],self.rain[3]) >= 30:
                self.c_text = self.d_text["r_23"]     #午後と夜の降水確率が30%以上
            elif self.rain[3] >= 30:
                self.c_text = self.d_text["r_3"]      #夜の降水確率が30%以上
            elif self.rain[2] >= 30:
                self.c_text = self.d_text["r_2"]      #午後の降水確率が30%以上
            else:
                self.c_text = self.d_text["nothing"]      #それ以外

        #気温の寒暖差が激しい場合
        elif int(self.kion_box[0]) - int(self.kion_box[1]) >= 15:
            self.c_text = self.d_text["kionsa"]

        #気温が低いとき
        elif int(self.kion_box[0]) <= 10:
            self.c_text = self.d_text["under10"]

        #気温が高いとき
        elif int(self.kion_box[0]) >= 30: self.c_text = self.d_text["over30"]

        #どの条件にも一致しなかった場合
        else: self.c_text = self.d_text["nothing"]


        #最終的な文章の合成
        self.f_text = self.aisatsu+"\n"+self.tenki+self.kion+"\n"+self.c_text+"\n"+"#デレマス朝の天気予報"
        print(self.f_text)
        print(len(self.f_text),"words")


if __name__ == "__main__":
    import datetime as dt
    xd = dt.datetime.today()
    xh = xd.hour
    if xh >= 0 and xh <= 12: x_num = 0
    else: x_num = 1

    import gt_v2 as p_gt
    gt = p_gt.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',"東京")
    cin = Mio(gt.gt_box_array[x_num],x_num)
    print("\n"+"#"*60)
    print("このモジュールは本田未央の「デレマス朝の天気予報」をお伝えします。")
    print("文字数のチェックを実施します。")
    print("="*60)
    print(cin.aisatsu,":",len(cin.aisatsu),"words")
    print(cin.tenki+cin.kion,":",len(cin.tenki+cin.kion),"words")
    print("残り文字数",140-len(cin.aisatsu)-len(cin.tenki+cin.kion)-11,"words")
    longest = ""
    for i in cin.d_text:
        if len(cin.d_text[i]) > len(longest): longest = cin.d_text[i]
        print("-"*60)
        print(i,":",cin.d_text[i],":",len(cin.d_text[i]),"words")
    print("-"*60)
    print("最長の文章は",":",longest,":",len(longest),"words")
