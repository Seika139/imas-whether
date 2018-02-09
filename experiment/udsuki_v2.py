#encoding:utf-8
import numpy.random as nmr

class  Udsuki:
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
        else:
            self.x_date = "明日"

        #挨拶の文章
        def aisatsu(self):
            if self.time == 0:
                self.aisatsu = "皆さんおはようございます！島村卯月の「デレマス朝の天気予報」のコーナーです。"
            else:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "こんばんは、島村卯月のお送りする{}の天気予報の時間です。".format(self.x_date)
                elif num == 1 : self.aisatsu = "こんばんは、島村卯月です。明日の天気予報をお伝えしますね！"
            return self.aisatsu

        self.aisatsu = aisatsu(self)


        self.tenki = "{}の{}の天気は「{}」、".format(self.x_date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報です。".format(self.kion_box[0],self.kion_box[1])

        #最後の天気によっって変化する文章の辞書
        self.d_text = {}
        if self.place == "仙台": self.d_text["nothing2"] = "続いて、東京の天気予報です。"
        elif self.place == "東京": self.d_text["nothing2"] = "続いて、大阪の天気予報です。"
        elif self.place == "大阪": self.d_text["nothing2"] = "続いて、福岡の天気予報です。"
        elif self.place == "福岡": self.d_text["nothing2"] = "以上、{}の天気予報でした。".format(self.x_date)
        if self.time == 0: self.d_text["nothing1"] = "それでは、今日も一日頑張っていきましょう！"
        else: self.d_text["nothing1"] = "今日も１日お疲れ様でした！"
        self.d_text["snow"] = "{}は雪が降る予報になっています。交通機関の情報にも注意して出かけてくださいね！".format(self.x_date)
        self.d_text["fine"] = "{}はよく晴れたいい天気になりそうで、私も頑張れそうです！皆さんも良い1日を〜♪".format(self.x_date)
        self.d_text["storm"] = "{}は強い雨と風が吹き荒れるようです。出かける際は十分に気をつけてくださいね！".format(self.x_date)
        self.d_text["r_123"] = "{}は1日を通じて降水確率が{}％を越えそうです。出かけるときは傘を忘れずに持っていきましょう".format(self.x_date,min(self.rain[1],self.rain[2],self.rain[3]))
        self.d_text["r_12"] = "{}は午前中の降水確率が{}％、午後は{}％となる見込みです。傘を忘れずに持っていきましょう。".format(self.x_date,self.rain[1],self.rain[2])
        self.d_text["r_23"] = "{}は午後の降水確率が{}％、夜は{}％となっています。傘を持っていくといいでしょう。".format(self.x_date,self.rain[2],self.rain[3])
        self.d_text["r_3"] = "{}は夜の降水確率が{}％となっています。帰りが遅い人は傘を持っていくといいでしょう。".format(self.x_date,self.rain[3])
        self.d_text["r_2"] = "{}は午後の降水確率が{}％となっています。傘があると良いでしょう。".format(self.x_date,self.rain[2])
        self.d_text["under10-1"] = "{}は冷え込むから、暖かい格好をして出かけましょう！".format(self.x_date)
        self.d_text["under10-2"] = "ちょっと寒いですね。冷え性の方は特に注意です！"
        self.d_text["under0-1"] = "{}度はちょっと寒すぎますね。温かい紅茶が飲みたいなあ"
        self.d_text["under0-2"] = "{}は寒いですね。私指先が冷えちゃうんです。えへへ".format(self.x_date)
        self.d_text["over30-1"] = "今度のオフは海に行きたいですね！えへへ"
        self.d_text["over30-2"] = "暑いので熱中症には気をつけてくださいね!"
        self.d_text["kionsa"] = "{}は気温差の激しい１日になります。服装に注意して出かけましょう".format(self.x_date)

        #何もない時の文章
        def nothing(self):
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["nothing1"]
            elif num == 1: self.c_text = self.d_text["nothing2"]
            return self.c_text

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
            else: self.c_text = nothing(self)      #それ以外

        #気温の寒暖差が激しい場合
        elif int(self.kion_box[0]) - int(self.kion_box[1]) >= 15:
            self.c_text = self.d_text["kionsa"]

        #最低気温が0度以下
        elif int(self.kion_box[1]) <= 0:
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["under0-1"]
            elif num == 1: self.c_text = self.d_text["under0-2"]

        #最高気温が10度以下
        elif int(self.kion_box[0]) <= 10:
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["under10-1"]
            elif num == 1: self.c_text = self.d_text["under10-2"]

        #気温が30度以上
        elif int(self.kion_box[0]) >= 30:
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["over30-1"]
            elif num == 1: self.c_text =  self.d_text["over30-2"]

        #どの条件にも一致しなかった場合
        else: self.c_text = nothing(self)


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
    import gt_v2
    gt = gt_v2.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',"東京")
    cin = Udsuki(gt.gt_box_array[x_num],x_num)
    print("\n"+"#"*60)
    print("このモジュールは島村卯月の「デレマス朝の天気予報」をお伝えします。")
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
