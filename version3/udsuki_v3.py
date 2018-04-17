import numpy.random as nmr
import datetime as dt
import common_function as cf

class Udsuki:
    def __init__(self,am_pm,japan,prediction,cond,s_data):

        self.place = prediction[0]
        self.weather = prediction[2]
        self.weather_id = prediction[3]
        self.kion_max = int(prediction[4][0])
        self.kion_min = int(prediction[4][1])
        self.rain = prediction[6]

        """ 1. 挨拶 """

        self.goodm_box = [
            "おはようございます！島村卯月による朝の天気予報のコーナーです。",
            "おはようございます！島村卯月です。朝の天気予報の時間ですよ！",
            "おはようございます、島村卯月のお送りする今日の天気予報の時間です。"
        ]
        self.goode_box = [
            "お仕事お疲れ様です。明日の天気予報を確認して明日に備えましょう！",
            "こんばんは、島村卯月のお送りする明日の天気予報の時間です。",
            "こんばんは、島村卯月です。明日の天気予報をお伝えしますね！"
        ]
        self.special =[
            'あけましておめでとうございます。今年もよろしくお願いします！',
            'ハッピーバレンタイン！島村卯月の天気予報ですよー',
            'あかりをつけましょ　ぼんぼりに～♪\n今日はひな祭りですね',
            'デレステ配信{}周年、おめでとうございます！天気予報の時間です！'.format(japan.year-2015),
            'ハッピーハロウィン！天気予報の時間ですよー',
            'モバマス配信{}周年、おめでとうございます！天気予報の時間ですよ'.format(japan.year-2011),
            'メリークリスマス！島村卯月の天気予報ですよー'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

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
        self.kion = "最高気温は{}度、最低気温は{}度の予報です。".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = [
            "{}は強い雨と風が吹き荒れるようです。出かける際は十分に気をつけてくださいね！".format(date),
            "ううっ、嵐が来るみたいですけど、大丈夫でしょうか？"
            ]
        self.d_text["rain_123"] = "{}は1日を通じて降水確率が{}％を越えそうです。出かけるときは傘を忘れずに持っていきましょう。".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "{}は午前中の降水確率が{}％、午後は{}％となる見込みです。雨具があるといいでしょう。".format(date,self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "{}は午後の降水確率が{}％、夜は{}％となっています。傘を持っていくといいでしょう。".format(date,self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％となっています。帰りが遅い人は傘を持っていくといいでしょう。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％となっています。傘があると良いでしょう。".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差の激しい１日になります。服装に注意して出かけましょう".format(date)
        self.d_text["under10"] = [
            "{}は冷え込むので、暖かい格好をして出かけましょう！".format(date),
            "ちょっと寒いですね。でも、レッスンしてると体が温まるんですよ！"
            ]
        self.d_text["under0"] = [
            "{}度はちょっと寒すぎますね。温かいお茶が飲みたいなあ".format(self.kion_min),
            '私、寒いと指先が冷えちゃって・・えへへ'
            ]
        self.d_text["over30"] = [
            'またみんなで海に行きたいですね！あ、でも水着を買わないと・・',
            '暑いので熱中症には気をつけてくださいね!',
            'どうしよう。スクール水着しか今着れる水着がないんですぅ〜'
            ]
        self.d_text["over25"] = [
            '最近アイスクリームを毎日食べちゃってて・・えへへ',
            '夜も25度を下回らないことを「熱帯夜」っていうんですよ。ご存知でしたか？'
            ]
        self.d_text["fine"] = "{}はよく晴れたいい天気になりそうで、私も頑張れそうです！皆さんも良い1日を〜♪".format(date)
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で一番低いようです。体調管理には気をつけてくださいね".format(date)
        self.d_text["w_cold_min"] = "{}はここ最近で一番冷え込むようです。体を冷やさないようにしてくださいね。".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はここ最近で一番暖かくなりますよ。気持ちのいい１日になりそうです。".format(date),
            1 : "{}はここ７日間で最も暑いです。熱中症には気をつけてくださいね。".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温がもっとも高くなりますよ。".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}は{}よりも{}度も暖かいようです。気温差に注意してくださいね。".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}は{}よりも{}度も暑くなりますよ。思い切って半袖で出かけてはどうでしょう！".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いようですよ。".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低くて、とても冷え込みそうです'.format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低くて、とても冷え込みそうです'.format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text['w_over30'] = '最近ずっと暑いので、熱中症には気をつけましょう。'
        self.d_text['w_under0'] = '最近は本当に寒くて…寝るときは湯たんぽを使うんですよ、私！'
        #雪が降る＆積雪が十分にある
        self.d_text['snow_1-10'] = {
            'term':'am_pm','cases':2,'border':1,
            0 : '現在の積雪は{}cmですが、さらに積もりそうですよ。'.format(s_data[3][0]),
            1 : "{}はさらに雪が積もりそうですよ！事務所で雪だるま作りたいです".format(date)
            }
        #雪が降る＆まあまあの積雪
        self.d_text['snow_1-1'] = {
            'term':'am_pm','cases':2,'border':1,
            0 : '現在の積雪は{}cmですが、さらに積もりそうですね。'.format(s_data[3][0]),
            1 : "{}の降雪でまた雪が積もるかもですね！".format(date)
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = "{}は雪が降るみたいですね。交通機関の情報にも注意してくださいね。".format(date)
        #雪が降らん＆積雪が十分にある
        self.d_text['snow_0-10'] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmです。雪の対策は大丈夫ですか？".format(s_data[3][0]),
            1 : "東京育ちの私にとっては、こんなに雪が積もるのは新鮮です！"
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "凍った雪は滑りやすいので気をつけてくださいね。"

        self.d_text['nothing_am']= [
            'それでは、今日も１日頑張っていきましょう！',
            '島村卯月、今日も１日頑張ります！',
            '夜の天気予報もチェックしてくださいね。'
            ]
        self.d_text['nothing_pm']= [
            'それでは、明日も頑張っていきましょう！',
            '今日も１日お疲れ様でした！',
            '明日の天気予報もチェックしてくださいね。'
            ]
        self.d_text['special'] = [
            '島村卯月、今年も頑張ります！',
            'ああ、あの…、チョコ受け取ってくれません…か？',
            '雛あられ食べますか？えへへ…',
            'これからもデレステをよろしくお願いします。',
            'トリックオアトリートですよ！お菓子をください！',
            '今後もモバマスをプレイしてくださいね！',
            '今年はサンタさんに何をもらえるのかなぁ。'
            ]

        if cond[1] == 0:
            self.c_text = cf.special_day(japan,self.d_text['special'])
            if self.c_text == None:
                if am_pm == 0: self.c_text = cf.rand_sel(self.d_text['nothing_am'])
                else: self.c_text = cf.rand_sel(self.d_text['nothing_pm'])
        elif type(self.d_text[cond[0]])==list: self.c_text = cf.rand_sel(self.d_text[cond[0]])
        elif type(self.d_text[cond[0]])==dict:
            x = self.d_text[cond[0]]
            if x['term'] == 'kion_max': elemnt = self.kion_max
            elif x['term'] == 'kion_min': elemnt = self.kion_min
            elif x['term'] == 'am_pm': elemnt = am_pm
            if elemnt >= x['border']: self.c_text = x[1]
            else: self.c_text = x[0]
        else: self.c_text = self.d_text[cond[0]]

        self.f_text = self.aisatsu+'\n'+self.tenki+self.kion+'\n'+self.c_text+'\n'+ht

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
    for j in range(7):
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
    cin = Udsuki(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは島村卯月の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
