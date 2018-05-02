#encoding:utf-8
import numpy.random as nmr
import datetime as dt

class Fumika:
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

        #月日の取得
        self.xdt = dt.datetime.today()
        self.sm = self.xdt.month
        self.sd = self.xdt.day

        #挨拶の文章
        def aisatsu(self):
            if self.time == 0:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "あ、あの、…鷺沢文香のお送りする天気予報の時間です…"
                else: self.aisatsu = "…おはようございます、鷺沢文香です。{}の天気予報をお伝えしますね…".format(self.x_date)
            else:
                num = nmr.randint(2)
                if num == 0: self.aisatsu = "あ、あの、…鷺沢文香のお送りする天気予報の時間です…"
                elif num == 1 : self.aisatsu = "…こんばんは、鷺沢文香です。{}の天気予報の時間です…".format(self.x_date)
            return self.aisatsu

        self.aisatsu = aisatsu(self)


        self.tenki = "{}の{}の天気は「{}」…、".format(self.x_date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報です…".format(self.kion_box[0],self.kion_box[1])

        #最後の天気によっって変化する文章の辞書
        self.d_text = {}
        if self.place == "仙台": self.d_text["nothing1"] = "続いては東京の天気です…"
        elif self.place == "東京": self.d_text["nothing1"] = "続いては大阪の天気です…"
        elif self.place == "大阪": self.d_text["nothing1"] = "続いては福岡の天気です…"
        elif self.place == "福岡": self.d_text["nothing1"] = "天気予報…{}もチェックしてくださいね…".format(self.x_date)
        if self.time == 0:
            self.d_text["nothing2"] = "春眠暁を覚えずとは言うものの、朝はいつでも眠いもので…"
            self.d_text["nothing3"] = "一日の計は朝にあり…と、早起きして良い一日を…"
        elif self.time == 1:
            self.d_text["nothing2"] = "ナイトプール…美波さんは泳ぎが達者で…"
            self.d_text["nothing3"] = "…本を読んでいたら、いつの間にか…夜に…"
        self.d_text["nothing4"] = "…あ、お勧めの本があれば、お教えください。ジャンルは…そうですね……"
        self.d_text["nothing5"] = "……最近は本屋と喫茶店が合わさったお店があるようで。"
        self.d_text["snow1"] =  "雪…。私の地元では、高く積もっていて…"
        self.d_text["snow2"] =  "蛍雪の功…？…いえ、私は読書が好きなだけで…"
        self.d_text["fine"] = "{}はいい天気になるようで…。たまには外に出て日差しを浴びるのも…".format(self.x_date)
        self.d_text["storm"] = "{}は荒れた天気の予報で…。晴耕雨読と言いますので、家で読書はいかがでしょうか…".format(self.x_date)
        self.d_text["r_123"] = "…{}は１日を通して降水確率が{}％を越えるようです。その…、傘を忘れずにお出かけください…".format(self.x_date,min(self.rain[1:]))
        self.d_text["r_12"] = "…午前中の降水確率が{}％、午後は{}％です。その…、雨具が必要ですよ…".format(self.rain[1],self.rain[2])
        self.d_text["r_23"] = "…午後の降水確率が{}％、夜は{}％です。雨が降ってなくても傘を持っていってください…".format(self.rain[2],self.rain[3])
        self.d_text["r_3"] = "…{}は夜の降水確率が{}％です。その…遅くまで外出する人は傘をお持ちに…".format(self.x_date,self.rain[3])
        self.d_text["r_2"] = "{}は午後の降水確率が{}％ですので…、出かける時は傘をお持ちください…".format(self.x_date,self.rain[2])
        self.d_text["under10-1"] = "{}は冷え込みますのでお体に気をつけて…".format(self.x_date)
        self.d_text["under10-2"] = "冬来たりなば春遠からじ…今は寒さに耐えましょう…"
        self.d_text["under0-1"] = "…{}は寒いですね。寒さ対策はしっかりと…".format(self.x_date)
        self.d_text["under0-2"] = "動かないと体が冷えますね…"
        self.d_text["over30-1"] = "今日はレッスン…暑いのがこたえますね…"
        self.d_text["over30-2"] = "…外は暑いですが、部屋の中は涼しくて…快適に読書ができます…"
        self.d_text["kionsa"] = "{}は気温差の激しい１日になると…。脱ぎ着のしやすい服装がよろしいかと…".format(self.x_date)

        #何もない時の文章
        def nothing(self):
            num = nmr.randint(5)
            if num == 0: self.c_text = self.d_text["nothing1"]
            elif num == 1: self.c_text = self.d_text["nothing2"]
            elif num == 2: self.c_text = self.d_text["nothing3"]
            elif num == 3: self.c_text = self.d_text["nothing4"]
            elif num == 4: self.c_text = self.d_text["nothing5"]
            return self.c_text

        #雪が降る場合
        if "雪" in self.weather and "雨か雪" not in self.weather:
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
    cin = Fumika(gt.gt_box_array[x_num],x_num)
    print("\n"+"#"*60)
    print("このモジュールは鷺沢文香の「デレマス朝の天気予報」をお伝えします。")
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
