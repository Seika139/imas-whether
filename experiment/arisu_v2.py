#encoding:utf-8
import numpy.random as nmr
import datetime as dt

class  Arisu:
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

        #1/15は苺の日
        self.xdt = dt.datetime.today()
        self.sm = self.xdt.month
        self.sd = self.xdt.day
        self.strawberry = False
        if self.sm == 1:
            if self.sd >= 10 and self.sd <= 15: self.strawberry == True

        #挨拶の文章
        def aisatsu(self):
            if self.time == 0:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "みなさん、起きてますか？{}の{}の天気予報です。".format(self.x_date,self.place)
                else: self.aisatsu = "おはようございます。橘ありすがお伝えする天気予報の時間です。"
            else:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "お仕事お疲れ様です。私、橘ありすが{}の天気予報をお送りします。".format(self.place)
                elif num == 1 : self.aisatsu = "こんばんは。橘ありすがお伝えする天気予報の時間です。"
            return self.aisatsu

        self.aisatsu = aisatsu(self)


        self.tenki = "{}の{}の天気は「{}」、".format(self.x_date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報です。".format(self.kion_box[0],self.kion_box[1])

        #最後の天気によっって変化する文章の辞書
        self.d_text = {}
        self.d_text["nothing1"] = "美味しいだけでなく美しい、私が目指すのはイチゴのようなアイドル…"
        if self.place == "仙台": self.d_text["nothing2"] = "続いて、東京の天気です。"
        elif self.place == "東京": self.d_text["nothing2"] = "続いて、大阪の天気です。"
        elif self.place == "大阪": self.d_text["nothing2"] = "続いて、福岡の天気です。"
        elif self.place == "福岡": self.d_text["nothing2"] = "天気予報、欠かさずチェックしてくださいね。".format(self.x_date)
        self.d_text["nothing3"] = "で、ですからありすではなく、橘と呼んでください！もう…"
        self.d_text["nothing4"] = "クールタチバナ、見せられましたか？"
        self.d_text["nothing5"] = "毎月22日はショートケーキの日です。なぜなら上にイチゴ(15)が乗ってますからね。"
        self.d_text["snow1"] =  "ゆ、雪ですか…私は子供みたいにはしゃぎませんよ…"
        self.d_text["snow2"] =  "雪…雪だるま…。な、何でもありません！"
        self.d_text["fine"] = "{}はいい天気になるようですが、どこかのプロデューサーみたいに浮かれてちゃダメですよ！".format(self.x_date)
        self.d_text["storm"] = "{}の天気は大荒れのようですが、レッスンならできます！".format(self.x_date)
        self.d_text["r_123"] = "{}は１日を通して降水確率が{}％を越えそうです。傘を忘れずに出かけましょう。".format(self.x_date,min(self.rain[1],self.rain[2],self.rain[3]))
        self.d_text["r_12"] = "午前中の降水確率が{}％、午後は{}％です。外出時には、傘を持って行ってください。".format(self.rain[1],self.rain[2])
        self.d_text["r_23"] = "午後の降水確率が{}％、夜は{}％です。雨が降ってなくても傘を持っていくのがよいでしょう。".format(self.rain[2],self.rain[3])
        self.d_text["r_3"] = "{}は夜の降水確率が{}％です。遅くまで外出する人は傘を持っていきましょう。".format(self.x_date,self.rain[3])
        self.d_text["r_2"] = "{}は午後の降水確率が{}％です。出かける時は傘を持っていきましょう。".format(self.x_date,self.rain[2])
        self.d_text["under10-1"] = "{}は冷え込むので、暖かい格好で出かけましょう。".format(self.x_date)
        self.d_text["under10-2"] = "寒い季節はイチゴが美味しいですね。まあ、いつでも美味しいんですけど…"
        self.d_text["under0-1"] = "{}は寒いから桃華さんに淹れ方を教わった紅茶を飲もうかな…".format(self.x_date)
        self.d_text["under0-2"] = "寒いのは苦手ですけど、プロとしてお仕事はちゃんとこなしますよ！"
        self.d_text["over30-1"] = "このぐらいの暑さでへばってるようじゃまだまだですね…"
        self.d_text["over30-2"] = "{}は暑いです。バテないように気をつけてくださいね。".format(self.x_date)
        self.d_text["kionsa"] = "{}は気温差の激しい１日になります。着脱が容易な服装で出かけましょう。".format(self.x_date)
        self.d_text["strawberry1"] = "1月15日はいちごの日です。是非、いちごを食べてくださいね！"
        self.d_text["strawberry2"] = "1月15日はいちごの日です。みなさん、いちごパスタはいかがですか？"

        #何もない時の文章
        def nothing(self):
            num = nmr.randint(5)
            if num == 0: self.c_text = self.d_text["nothing1"]
            elif num == 1: self.c_text = self.d_text["nothing2"]
            elif num == 2: self.c_text = self.d_text["nothing3"]
            elif num == 3: self.c_text = self.d_text["nothing4"]
            elif num == 4: self.c_text = self.d_text["nothing5"]
            return self.c_text

        #苺の日が近い場合
        if self.strawberry == True:
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["strawberry1"]
            elif num == 0: self.c_text = self.d_text["strawberry2"]

        #雪が降る場合
        elif "雪" in self.weather and "雨か雪" not in self.weather:
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["snow1"]
            elif num == 1: self.c_text = self.d_text["snow2"]

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

        #ショートケーキの日
        elif self.sd == 22 or self.sd == 15: self.c_text = self.d_text["nothing5"]

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
    cin = Arisu(gt.gt_box_array[x_num],x_num)
    print("\n"+"#"*60)
    print("このモジュールは橘ありすの「デレマス朝の天気予報」をお伝えします。")
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
