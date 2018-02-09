#encoding:utf-8
import numpy.random as nmr
import datetime as dt

class  Yoshino:
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

        #桜の開花時期
        self.xdt = dt.datetime.today()
        self.sm = self.xdt.month
        self.sd = self.xdt.day
        self.sakura = False
        if self.sm == 3:
            if self.sd >= 25: self.sakura == True
        elif self.sm == 4:
            if self.sd  <= 15: self.sakura == True

        #挨拶の文章
        def aisatsu(self):
            if self.time == 0:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "みなさまー、お目覚めですか？依田芳乃の天気予報の時間でしてー"
                else: self.aisatsu = "おはようございますー。わたくし依田は芳乃が、{}の天気をお伝えするのでしてー".format(self.x_date)
            else:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "お仕事お疲れ様ですー。今宵の依田芳乃の天気予報の時間でしてー"
                elif num == 1 : self.aisatsu = "こんばんはー。わたくし依田は芳乃が、{}の天気をお伝えするのでしてー".format(self.x_date)
            return self.aisatsu

        self.aisatsu = aisatsu(self)


        self.tenki = "{}の{}の天気は「{}」、".format(self.x_date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度となるでしょうー。".format(self.kion_box[0],self.kion_box[1])

        #最後の天気によっって変化する文章の辞書
        self.d_text = {}
        self.d_text["nothing1"] = "そなたに失せ物があれば、わたくしが探しますゆえー"
        if self.place == "仙台": self.d_text["nothing2"] = "続いては東京の天気予報でしてー"
        elif self.place == "東京": self.d_text["nothing2"] = "続いては大阪の天気予報でしてー"
        elif self.place == "大阪": self.d_text["nothing2"] = "続いては福岡の天気予報でしてー"
        elif self.place == "福岡": self.d_text["nothing2"] = "以上が{}の天気予報でしてー".format(self.x_date)
        self.d_text["nothing3"] = "そなたのお力になれましたでしょうかー？"
        self.d_text["nothing4"] = "法螺貝には魔を払う力があるのでしてー。ぷおー、ぶおー"
        self.d_text["snow"] =  "雪の花が街を彩るのでしてー"
        self.d_text["fine"] = "{}は良き天気になるようでしてー。日輪の恵みを、その手にー".format(self.x_date)
        self.d_text["storm"] = "{}は天気が優れないゆえー、なるべく外出はお控えくださいませー".format(self.x_date)
        self.d_text["r_123"] = "{}は１日を通して降水確率が{}％を越えそうなので傘が必要でしてー".format(self.x_date,min(self.rain[1],self.rain[2],self.rain[3]))
        self.d_text["r_12"] = "午前中の降水確率が{}％、午後は{}％でしてー。傘を持っていくのがよいかとー".format(self.rain[1],self.rain[2])
        self.d_text["r_23"] = "午後の降水確率が{}％、夜は{}％でしてー。雨が降ってなくても傘を持たれるのがよいかとー".format(self.rain[2],self.rain[3])
        self.d_text["r_3"] = "{}は夜の降水確率が{}％でしてー。遅くまで外出する人は傘を持たれるのがよいかとー".format(self.x_date,self.rain[3])
        self.d_text["r_2"] = "{}は午後の降水確率が{}％でしてー。出かける時は傘を持たれるのがよいかとー".format(self.x_date,self.rain[2])
        self.d_text["under10-1"] = "{}は冷え込みますゆえー、暖かい格好で出かけなさいませー".format(self.x_date)
        self.d_text["under10-2"] = "寒い日の温泉は温かさがより染み渡るのでしてー"
        self.d_text["under0-1"] = "厚めのこーとを着ましょうー、寒さが厳しいゆえー"
        self.d_text["under0-2"] = "指先が冷たくとも、心はほかほか温かいのでしてー"
        self.d_text["over30-1"] = "過ぎたるは猶及ばざるが如し…と言う様にー、冷房のつけすぎは、逆に体に良くないのでしてー"
        self.d_text["over30-2"] = "この暑き日ー、熱中症には気をつけくださいませー"
        self.d_text["kionsa"] = "{}は気温差の激しい１日になりますゆえー。お体を壊さぬよう、気をつけくださいませー".format(self.x_date)
        self.d_text["sakura1"] = "みなの住まう所では、桜は咲いてますでしょうかー？こちらの桜は綺麗でしてー"
        self.d_text["sakura2"] = "{}は紗枝さんとお花見にいくのでしてー".format(self.x_date)

        #何もない時の文章
        def nothing(self):
            num = nmr.randint(4)
            if num == 0: self.c_text = self.d_text["nothing1"]
            elif num == 1: self.c_text = self.d_text["nothing2"]
            elif num == 2: self.c_text = self.d_text["nothing3"]
            elif num == 3: self.c_text = self.d_text["nothing4"]
            return self.c_text

        #桜の場合
        if self.sakura == True and "晴れ" in self.weather:
            num = nmr.randint(2)
            if num == 0: self.c_text = self.d_text["sakura1"]
            elif num == 0: self.c_text = self.d_text["sakura2"]

        #雪が降る場合
        elif "雪" in self.weather and "雨か雪" not in self.weather:
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
        self.f_text = self.aisatsu+"\n"+self.tenki+self.kion+"\n"+self.c_text+"\n"+self.ht
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
    cin = Yoshino(gt.gt_box_array[x_num],x_num)
    print("\n"+"#"*60)
    print("このモジュールは依田芳乃の「デレマス朝の天気予報」をお伝えします。")
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
