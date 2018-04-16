import numpy.random as nmr
import datetime as dt
import common_function as cf

class Sachiko:
    def __init__(self,am_pm,japan,prediction,cond,s_data):

        self.place = prediction[0]
        self.weather = prediction[2]
        self.weather_id = prediction[3]
        self.kion_max = int(prediction[4][0])
        self.kion_min = int(prediction[4][1])
        self.rain = prediction[6]

        """ 1. 挨拶 """

        self.goodm_box = [
            "ふふーん！ボクの天気予報を見れるなんてあなたは幸せ者ですねぇー",
            "みなさーん、カワイイ幸子による天気予報ですよ！",
            "え、カワイイボクよりも天気が気になる？しょうがないですねー",
            "おはようございまーす！輿水幸子の天気予報の時間ですよー"
        ]
        self.goode_box = [
            "ふふーん！ボクの天気予報を見れるなんてあなたは幸せ者ですねぇー",
            "みなさーん、カワイイ幸子による天気予報ですよ！",
            "え、カワイイボクよりも天気が気になる？しょうがないですねー",
            "こんばんはー！輿水幸子の天気予報の時間ですよー"
        ]
        self.special =[
            'フフーン！！あけましておめでとうございます！',
            'ハッピーバレンタイン！輿水幸子の天気予報ですよー',
            'ふふーん！今日は女の子の祭典、ひな祭りですよ！',
            'ふふーん！デレステ配信{}周年ですよ♪'.format(japan.year-2015),
            'ハッピーハロウィン！今日の気予報の時間ですよー',
            'ふふーん！モバマス配信{}周年ですよ！'.format(japan.year-2011),
            'メリークリスマス！輿水幸子の天気予報ですよ！'
            ]

        if japan.month==1 and japan.day<=3:
            self.aisatsu = self.special[0]
        elif japan.month==2 and japan.day==14:
            self.aisatsu = self.special[1]
        elif japan.month==3 and japan.day==3:
            self.aisatsu = self.special[2]
        elif japan.month==9 and 3<=japan.day<=5:
            self.aisatsu = self.special[3]
        elif japan.month==10 and japan.day==31:
            self.aisatsu = self.special[4]
        elif japan.month==11 and 28<=japan.day<=30:
            self.aisatsu = self.special[5]
        elif japan.month==12 and 24<=japan.day<=25:
            self.aisatsu = self.special[6]
        else:
            if am_pm == 0:
                num = nmr.randint(len(self.goodm_box))
                self.aisatsu = self.goodm_box[num]
            else:
                num = nmr.randint(len(self.goode_box))
                self.aisatsu = self.goode_box[num]

        """ 2. 予報 """

        if am_pm == 0:
            date = "今日"
            pre_date = "昨日"
            ht = "#デレマス朝の天気予報"
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報です！".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""
        def rbs(x):
            y = round(abs(x),1)
            return y

        self.d_text = {}
        self.d_text["storm"] = [
            "嵐がきたぐらいじゃボクのカワイさはびくともしません！",
            "ふふーん！嵐なんてどんと来いです！"
            ]
        self.d_text["rain_123"] = "{}は降水確率が一日中{}％を越えるようです！出かけるときは傘が必要ですよ〜".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "午前中の降水確率が{}％、午後は{}％です。雨具が必要ですよ！".format(self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％です。雨が降ってなくても傘が要るかもですよ！".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％です。遅くまで外出する人は傘を持って行きましょう！".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％です。傘があるといいでしょう。".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差のある一日です。脱ぎ着のしやすい服装がいいですよ！".format(date)
        self.d_text["under10"] = [
            "寒さなんて、ボクの前では無力です。フフーン！",
            'このくらいの寒さならボクは大丈夫ですよ！？'
            ]
        self.d_text["under0"] = [
            'ひぃ、この寒さは北海道のロケを思い出しますねぇ',
            'ちょっと！寒中水泳のロケは嫌ですってばー！'
            ]
        self.d_text["over30"] = [
            'いやぁ、暑い日は海に限りますね！え？泳げますよ！と、当然です！',
            '暑くて外に出られないなんて、だらしないですよ。ほらほら♪'
            ]
        self.d_text["over25"] = [
            '暑くて眠れない夜はボクを数えてください！ほら、カワイイ幸子が１人、カワイイ幸子が２人...',
            '水分をきちんと摂って寝るのがカワイさの秘訣ですよ♪'
            ]
        self.d_text["fine"] = "フフーン！{}はカワイイボクに相応しい良い天気になりそうですね！".format(date)
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で一番低いようですよ！".format(date)
        self.d_text["w_cold_min"] = "{}はここ最近で一番冷え込むようですよ。暖かい格好で出かけましょう！".format(date)
        if self.kion_max >= 25:
            self.d_text["w_hot_max"] = "{}はここ最近で一番の暑さです！熱中症には気をつけましょう！".format(date)
        else:
            self.d_text["w_hot_max"] = "{}はここ最近で一番暖かいようです。普段より涼しめな格好でいいかもしれませんね。".format(date)
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温がもっとも高くなるようですよ〜".format(date)
        if self.kion_max >= 25:
            self.d_text["y_hot_max"]="{}は{}よりも{}度も暑いようですねぇ。暑さに気をつけてくださいね〜".format(date,pre_date,rbs(self.kion_max-s_data[0][0]))
        else:
            self.d_text["y_hot_max"] = "{}は{}よりも{}度も暖かいようですねぇ。ふふーん！".format(date,pre_date,rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いようですねぇ。ふふーん！".format(date,pre_date,rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低くて、とても冷え込みそうですねぇ'.format(date,pre_date,rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低くて、とても冷え込みそうですねぇ'.format(date,pre_date,rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = "{}はさらに雪が積もりそうですよ！ふふーん！".format(date)
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = "{}はさらに雪が積もりそうですよ！ふふーん！".format(date)
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = "別にボクは雪が降ったぐらいじゃしゃぎませんよ。ふーんだ！"
        #雪が降らん＆積雪が十分にある
        if am_pm == 0: self.d_text["snow_0-10"] = "現在の積雪は{}cmですよ。雪用の靴を履きましょう！".format(s_data[3][0])
        else: self.d_text["snow_0-10"] = "雪が積もっているので雪用の靴を履きましょう！"
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "まだまだ雪は解けてませんよ。滑って転ばないでくださいね！"

        self.d_text['nothing_am']= [
            'さてさて、明日の小テストの勉強をしなくては！',
            'ふふーん！皆さんも良い一日を〜♪',
            '夜の天気予報もチェックしてくださいね〜'
            ]
        self.d_text['nothing_pm']=[
            'さてさて、明日の小テストの勉強をしなくては！',
            'ふふーん！皆さんおやすみなさ〜い',
            '明日の天気予報もチェックしてくださいね〜'
            ]
        self.d_text['special'] = [
            '今年も天気予報をみてくださいよ！',
            'フフーン、',
            '私がお雛様なら、お内裏様は…あの人かな…',
            'これからもデレステをよろしくね。',
            'ハロウィンだからって…そんなに浮かれすぎちゃダメだよ。',
            'いつもモバマスをプレイしてくれてありがとう…',
            '

        if cond[1] == 0:
            if japan.month==1 and japan.day<=3:
                self.c_text = self.d_text['special'][0]
            elif japan.month==2 and japan.day==14:
                self.c_text = self.d_text['special'][1]
            elif japan.month==3 and japan.day==3:
                self.c_text = self.d_text['special'][2]
            elif japan.month==9 and 3<=japan.day<=5:
                self.c_text = self.d_text['special'][3]
            elif japan.month==10 and japan.day==31:
                self.c_text = self.d_text['special'][4]
            elif japan.month==11 and 28<=japan.day<=30:
                self.c_text = self.d_text['special'][5]
            elif japan.month==12 and 24<=japan.day<=25:
                self.c_text = self.d_text['special'][6]
            elif am_pm == 0:
                self.c_text = self.d_text['nothing_am'][nmr.randint(len(self.d_text['nothing_am']))]
            else:
                self.c_text = self.d_text['nothing_pm'][nmr.randint(len(self.d_text['nothing_pm']))]
        elif type(self.d_text[cond[0]])==list:
            self.c_text = self.d_text[cond[0]][nmr.randint(len(self.d_text[cond[0]]))]
        else:
            self.c_text = self.d_text[cond[0]]

        self.f_text = self.aisatsu+'\n'+self.tenki+self.kion+'\n'+self.c_text+'\n'+ht

    #文字数の確認
    def length_check(self,show):
        print()
        def show_text(text):
            if show =="1": print(text)
        def mini_check(length,box):
            longest = 0
            text = ""
            if type(box)==list:
                for i in box:
                    show_text(str(len(i))+': '+i)
                    if len(i) >= longest:
                        longest = len(i)
                        text = i
            elif type(box)==dict:
                for i in box:
                    if type(box[i])==list:
                        for j in box[i]:
                            show_text(str(len(j))+': '+j)
                            if len(j) >= longest:
                                longest = len(j)
                                text = j
                    else:
                        show_text(str(len(box[i]))+': '+box[i])
                        if len(box[i]) >= longest:
                            longest = len(box[i])
                            text = box[i]
            if longest > length:
                print("最長のものが{}文字で規定の長さ{}文字を超えています。".format(longest,length))
                print("最長の文章は\n",text)
            else:
                print("最長のものが{}文字なので規定の長さ{}文字以内を満たしています。".format(longest,length))
            print("-"*50)

        print("<< goodm_boxの確認 >>")
        mini_check(33,self.goodm_box)
        print("<< goode_boxの確認 >>")
        mini_check(33,self.goode_box)
        print("<< specialの確認 >>")
        mini_check(33,self.special)
        print("<< text2の確認 >>")
        print(len(self.tenki+self.kion),"words　(45文字以下ならOK)")
        print("-"*50)
        print("<< d_textの確認 >>")
        mini_check(48,self.d_text)



if __name__ == "__main__":

    import datetime as dt
    now = dt.datetime.now()
    japan = now + dt.timedelta(hours=0)
    j_hour = japan.hour
    if 0 <= j_hour <= 12: am_pm = 0
    else: am_pm = 1

    import recorder as rc
    import gt_v3
    gt = gt_v3.Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',"東京")
    data_base = []
    for j in range(10):
        previous = japan - dt.timedelta(days=j+1-am_pm)
        rcd = rc.Recorder("東京",previous)
        rcd.get_info()
        rcd.add_to_excel()
        rcd.eroor_check()
        data_base.append(rcd.get_data(previous))

    if am_pm == 1:
        data_base[0]["day"] = japan.day
        data_base[0]["気温"]["最高"] = float(gt.gt_box_array[0][4][0])
        data_base[0]["気温"]["最低"] = float(gt.gt_box_array[0][4][1])
        data_base[0]["天気概況"]["昼"] = gt.gt_box_array[0][2]

    import condition_setter as cs
    setter = cs.Setter(am_pm,data_base,gt.gt_box_array[am_pm])
    cin = Sachiko(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは輿水幸子の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [
        cin.goodm_box,
        cin.goode_box,
        cin.special,
        cin.tenki,
        cin.kion,
        cin.d_text
    ]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
