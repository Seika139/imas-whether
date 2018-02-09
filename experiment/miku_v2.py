#encoding:utf-8
import numpy.random as nmr

class Miku:
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
            self.ht = "#デレマス朝の天気予報"
        else:
            self.x_date = "明日"
            self.ht = "#デレマス夜の天気予報"


        #挨拶の文章
        def aisatsu(self):
            if self.time == 0:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "おっはよ〜！{}の天気予報をこのみくがお送りするにゃ！".format(self.x_date)
                elif num == 1 : self.aisatsu = "みんな、おはよ〜！みくのにゃんにゃん天気予報始まるよー"
            else:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "こんばんにゃあ！{}の天気予報をこのみくがお送りするにゃ！".format(self.x_date)
                elif num == 1 : self.aisatsu = "みんな、お疲れ〜！みくのにゃんにゃん天気予報の時間だよ〜"
            return self.aisatsu

        self.aisatsu = aisatsu(self)


        self.tenki = "{}の{}の天気は「{}」、".format(self.x_date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度だにゃ。".format(self.kion_box[0],self.kion_box[1])

        #最後の天気によっって変化する文章の辞書
        self.d_text = {}
        if self.time == 0: self.d_text["nothing1"] = "今日もお仕事頑張ってね♪"
        else: self.d_text["nothing1"] = "今日もお仕事お疲れ様♪"
        self.d_text["nothing2"] = "にゃふふ♪今日のねこみみもイケてるにゃ！"
        self.d_text["nothing3"] = "ちょっと！お魚の入ってるお弁当はダメって言ったにゃ〜！！"
        self.d_text["snow"] = "雪やこんこん♪雪の日、ネコちゃんはこたつで丸くなるにゃ〜"
        self.d_text["fine"] = "うーん、いい天気だにゃあ…ムニャムニャ…\nハッ！ね、寝てないもん！"
        self.d_text["storm"] = "こんな天気だと尻尾が濡れちゃうから困るにゃ〜"
        self.d_text["r_123"] = "{}は一日中降水確率が{}％を越えそうだから傘が必要だにゃ。".format(self.x_date,min(self.rain[1],self.rain[2],self.rain[3]))
        self.d_text["r_12"] = "{}は午前中の降水確率が{}％、午後は{}％だって…傘を忘れずに持っていくにゃあ".format(self.x_date,self.rain[1],self.rain[2])
        self.d_text["r_23"] = "午後の降水確率が{}％、夜は{}％だから、雨が降ってなくても、傘を持っていくにゃ！".format(self.rain[2],self.rain[3])
        self.d_text["r_3"] = "{}は夜の降水確率が{}％。夕方から雨が降りそうだから傘を持って出かけるにゃあ。".format(self.x_date,self.rain[3])
        self.d_text["r_2"] = "{}は午後の降水確率が{}％だよ。傘を持っていくといくにゃあ".format(self.x_date,self.rain[2])
        self.d_text["under10-1"] = "フゥー…寒いにゃあ。みくも毛皮があれば〜"
        self.d_text["under10-2"] = "寒いけど、みくは元気にゃ〜！"
        self.d_text["under0-1"] = "{}度は寒すぎるにゃ〜。鳥肌、いや、猫肌が立つにゃ！".format(self.kion_box[1])
        self.d_text["under0-2"] = "{}は寒いよ〜。猫カフェでゆっくり温まりたいにゃあ".format(self.x_date)
        self.d_text["over30-1"] = "あったかいのは好きだけど、{}は暑すぎるにゃあ".format(self.x_date)
        self.d_text["over30-2"] =  "にゃー、暑いよ〜お水が欲しいにゃあ"
        self.d_text["kionsa"] = "{}は気温差の激しい１日になるから服装に注意するにゃ！".format(self.x_date)


        #何もない時の文章
        def nothing(self):
            num = nmr.randint(3)
            if num == 0: self.c_text = self.d_text["nothing1"]
            elif num == 1: self.c_text = self.d_text["nothing2"]
            elif num == 2: self.c_text = self.d_text["nothing3"]
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

        #気温が0度以下
        elif int(self.kion_box[1]) <= 0:
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["under0-1"]
            elif num == 1: self.c_text = self.d_text["under0-2"]

        #気温が10度以下
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
        self.f_text = self.aisatsu+"\n"+self.tenki+self.kion+"\n"+self.c_text+"\n"+self.ht
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
    cin = Miku(gt.gt_box_array[x_num],x_num)
    print("\n"+"#"*60)
    print("このモジュールは前川みくの「デレマス朝の天気予報」をお伝えします。")
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
