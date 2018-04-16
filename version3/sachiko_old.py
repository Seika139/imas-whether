#encoding:utf-8
import numpy.random as nmr
import datetime as dt
#from operator import itemgetter

class Sachiko:
    def __init__(self,box,time,record):

        self.place = box[0] #　"東京"
        self.reporting_date = box[1] # 2018/03/15
        self.weather = box[2] # 晴れ時々くもり
        self.weather_id = box[3] # http://www.drk7.jp/MT/images/MTWeather/101.gif
        self.kion_box = box[4] # ['22', '8']
        self.jikantai = box[5] # ['00-06', '06-12', '12-18', '18-24']
        self.rain = box[6] #降水確率 [10,10,10,10] の形
        self.time = time #0か1　0なら朝の天気予報、1なら夜の天気予報

        self.r_kion_max = []
        self.r_kion_min =[]
        self.r_snow_fall = []
        self.r_snow_depth = []
        self.r_tenki = []
        self.sunshine_hour = []
        for i in renge(len(record)):
            self.r_kion_max.append(record[i]["気温"]["最高"])
            self.r_kion_min.append(record[i]["気温"]["最低"])
            self.r_snow_fall.append(record[i]["雪"]["降雪"])
            self.r_snow_depth.appned(record[i]["雪"]["最深積雪"])
            self.r_tenki.append(record[i]["天気概況"]["昼"])
            self.sunshine_hour.append(record[i]["日照時間"])

"""
雪
気温差
天気の変化
昨日とは違って
ここ数日とは違って
elifをなるべくifにする
優先度を導入しc_text_arrayに全部追加し、優先度の高いものをc_textとする
"""
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

""" text 1 挨拶 """

        #挨拶の文章
        def aisatsu(self):
            num = nmr.randint(4)
                if num == 0: self.aisatsu = "ふふーん！ボクの天気予報を見れるなんてあなたは幸せ者ですねぇー"
                elif num == 1: self.aisatsu = "みなさーん、カワイイ幸子による天気予報ですよ！"
                elif num == 2: self.aisatsu = "え、カワイイボクよりも天気が気になる？しょうがないですねー"
                else:
                    if self.time == 0: self.aisatsu = "おはようございまーす！輿水幸子の天気予報の時間ですよー"
                    else: self.aisatsu = "こんばんはー！輿水幸子の天気予報の時間ですよー"
            return self.aisatsu

        self.aisatsu = aisatsu(self)

""" text 2 予報 """
        self.tenki = "{}の{}の天気は「{}」、".format(self.x_date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報です！".format(self.kion_box[0],self.kion_box[1])

""" text 3 締め """
        #最後の天気によっって変化する文章の辞書
        self.c_text_array = []
        self.d_text = {}
        if self.place == "仙台": self.d_text["nothing1"] = "続いては東京の天気です…"
        elif self.place == "東京": self.d_text["nothing1"] = "続いては大阪の天気です…"
        elif self.place == "大阪": self.d_text["nothing1"] = "続いては福岡の天気です…"
        elif self.place == "福岡": self.d_text["nothing1"] = "天気予報…明日もチェックしてくださいね…".format(self.x_date)
        if self.time == 0:
            self.d_text["nothing2"] = "春眠暁を覚えずとは言うものの、朝はいつでも眠いもので…"
            self.d_text["nothing3"] = "一日の計は朝にあり…と、早起きして良い一日を…"
        elif self.time == 1:
            self.d_text["nothing2"] = "ナイトプール…美波さんは泳ぎが達者で…"
            self.d_text["nothing3"] = "…本を読んでいたら、いつの間にか…夜に…"
        self.d_text["nothing4"] = "…あ、お勧めの本があれば、お教えください。ジャンルは…そうですね……"
        self.d_text["nothing5"] = "……最近は本屋と喫茶店が合わさったお店があるようで。"
        self.d_text["snow1"] =  "別にボクは雪が降ったぐらいじゃしゃぎませんよ〜"
        self.d_text["snow2"] =  "ボクの地元も一応雪国なんですよ。スキーは…苦手ですけど…"
        self.d_text["fine"] = "フフーン！{}はカワイイボクに相応しい良い天気になりそうですね！".format(self.x_date)
        self.d_text["storm"] = "嵐がきたぐらいじゃボクのカワイさはびくともしません！"
        self.d_text["r_123"] = "{}は降水確率が一日中{}％を越えるようです！出かけるときは傘が必要ですよ〜".format(self.x_date,min(self.rain[1],self.rain[2],self.rain[3]))
        self.d_text["r_12"] = "午前中の降水確率が{}％、午後は{}％です。雨具が必要ですよ！".format(self.rain[1],self.rain[2])
        self.d_text["r_23"] = "午後の降水確率が{}％、夜は{}％です。雨が降ってなくても傘が要るかもですよ〜".format(self.rain[2],self.rain[3])
        self.d_text["r_3"] = "{}は夜の降水確率が{}％です。遅くまで外出する人は傘を持って行きましょう！".format(self.x_date,self.rain[3])
        self.d_text["r_2"] = "{}は午後の降水確率が{}％です。傘があるといいでしょう。".format(self.x_date,self.rain[2])
        self.d_text["under10-1"] = "{}は冷え込みますのでお体に気をつけて…".format(self.x_date)
        self.d_text["under10-2"] = "寒さなんて"
        self.d_text["under0-1"] = "…{}は寒いですね。寒さ対策はしっかりと…".format(self.x_date)
        self.d_text["under0-2"] = "寒さなんて、ボクの前では無力です！フフーン"
        self.d_text["over30-1"] = "いやぁ、暑い日は海に限りますね！え？泳げますよ！と、当然です！"
        self.d_text["over30-2"] = "暑くて外に出られないなんて、だらしないですよ。ほらほら♪"
        self.d_text["kionsa"] = "{}は気温差のある一日です。脱ぎ着のしやすい服装がいいですよ！".format(self.x_date)
        self.d_text["積雪1"] = "現在{}cmの積雪がありますが、さらに積もるかもしれませんよ！".format(self.r_snow_depth[0])
        self.d_text["積雪10"] = "積雪{}cmなので出かけるときは気をつけてくださいね〜♪".format(self.r_snow_depth[0])
        self.d_text["残雪"] = "まだまだ雪は解けてませんよ。滑って転ばないでくださいね！"

        #何もない時の文章
        def nothing(self):
            num = nmr.randint(5)
            if num == 0: c_text = self.d_text["nothing1"]
            elif num == 1: c_text = self.d_text["nothing2"]
            elif num == 2: c_text = self.d_text["nothing3"]
            elif num == 3: c_text = self.d_text["nothing4"]
            elif num == 4: c_text = self.d_text["nothing5"]
            return c_text

        # 雪
        if "雪" in self.weather and "雨か雪" not in self.weather:
            if type(self.r_snow_depth[0]) == float:
                if self.r_snow_depth[0] >= 10:
                    self.c_text_array.append(self.d_text["積雪10"])
                elif self.r_snow_depth[0] >= 1:
                    self.c_textself.d_text["積雪1"]
            else:
                num = nmr.randint(2)
                if num == 0: self.c_text = self.d_text["snow1"]
                elif num == 1: self.c_text = self.d_text["snow2"]

        elif type(self.r_snow_depth[0]) == float:
            if self.r_snow_depth[0] >= 10:
                self.c_text = self.d_text["積雪10"]
            elif: "晴" in self.weather and self.r_snow_depth[0] < 5:
                self.c_text = self.d_text["残雪"]
            else:
                try:
                    if self.r_snow_depth[0] <=  self.r_snow_depth[1] and self.r_snow_depth[1] <=  self.r_snow_depth[2]:
                        self.c_text = self.d_text["残雪"]

        #強い雨が降る場合
        elif "307" in self.weather_id or "308" in self.weather_id:
            self.c_text = self.d_text["storm"]

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

        #久々の晴れ
        elif self.time == 0 and type(self.sunshine_hour[0]) == float and type(self.sunshine_hour[1]) == float:

        elif self.time == 1 and

        #気温の寒暖差が激しい場合
        elif int(self.kion_box[0]) - int(self.kion_box[1]) >= 12:
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

        #ただの「晴れ」の場合
        elif "100" in self.weather_id:
            self.c_text = self.d_text["fine"]
        #どの条件にも一致しなかった場合
        else: self.c_text = nothing(self)

        if self.c_text == "":
            self.c_text = nothing(self)

        self.c_text_array.sort(key=itemgetter(1))

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

    data_base = []
    for j in range(7):
        pre = japan - dt.timedelta(days=j+1)
        pre_array = [pre.year,pre.month,pre.day,pre.hour,pre.minute]
        rcd = rc.Recorder(place_box[1],pre_array)
        data_base.append(rcd.get_data(pre_array[2]))

    import gt_v3
    gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',"東京")
    cin = Sachiko(gt.gt_box_array[x_num],x_num,data_base)
    print("\n"+"#"*60)
    print("このモジュールは輿水幸子の「デレマス朝の天気予報」をお伝えします。")
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
