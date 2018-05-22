import numpy.random as nmr
import datetime as dt
import common_function as cf

class Rin:
    def __init__(self,am_pm,japan,prediction,cond,s_data):

        self.place = prediction[0]
        self.weather = prediction[2]
        self.weather_id = prediction[3]
        self.kion_max = int(prediction[4][0])
        self.kion_min = int(prediction[4][1])
        self.rain = prediction[6]

        if am_pm == 0:
            date = "今日"
            pre_date = "昨日"
            ht = "#デレマス朝の天気予報"
            greet = 'おはよう'
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"
            greet = 'こんばんは'

        """ 1. 挨拶 """

        self.goodm_box = [
            "みんなおはよう…渋谷凛です。今日の天気予報をお知らせします。",
            "ふふっ、今朝の天気予報は私、渋谷凛がお送りします。",
            "おはようございます…渋谷凛のお送りする朝の天気予報です。"
            ]
        self.goode_box = [
            "ほらほら、寝る前に明日の天気と予定の確認はしといてよね。",
            "こんばんは、渋谷凛のお送りする明日の天気予報の時間です。",
            "こんばんは…渋谷凛です。明日の天気を教えてあげるね。"
            ]
        self.special =[
            'あけましておめでとう…新年の天気予報だよ。',
            '今日はバレンタインだけど…天気予報も忘れずにね',
            '{}、今日はひな祭りだよ。覚えてた？'.format(greet),
            '９月３日でデレステ配信{}周年、めでたい日だね。'.format(japan.year-2015),
            '今日はハロウィンだけど…天気予報も忘れずにね',
            '１１月２８日でモバマス配信{}周年だね、おめでとう'.format(japan.year-2011),
            'メリークリスマス！ふふっ、渋谷凛の天気予報です。'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報です。".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = [
            "{}は雨も風も強いみたい…出かけるときは気をつけてね。".format(date),
            "雷は落ちてこないで、ハナコが怖がるから…"
            ]
        self.d_text["rain_123"] = "{}は1日を通じて降水確率が{}％を越えそうだから、出かけるときは傘を忘れずにね。".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "{}は午前中の降水確率が{}％、午後は{}％となる見込みだよ。傘を忘れずに持っていってね。".format(date,self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "{}は午後の降水確率が{}％、夜は{}％だから、雨が降ってなくても傘を持っていくといいかもね。".format(date,self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％。夕方から雨が降りそうだよ…帰りが遅い人は傘を忘れずにね。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％だよ。雨で濡れないように…気をつけてね".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差の激しい１日になるよ。服装に注意してね…".format(date)
        self.d_text["under10"] = [
            "{}は冷え込むから、暖かい格好をして出かけてね。".format(date),
            "みんなは寒い？新しいマフラー買おうかな…"
            ]
        self.d_text["under0"] = [
            "{}度って…ちょっと寒すぎない？".format(self.kion_min),
            '寒い夜もハナコが布団に入ってくると温かいんだ…'
            ]
        self.d_text["over30"] = [
            '裸足で砂浜を歩く…なんかリアルが感じらる気がして…',
            '大丈夫？暑いときは無理しないでね…',
            '会場の熱気の方が熱いから…負けてられない！',
            "{}は暑いね…海、行きたくなってきたかも…".format(date)
            ]
        self.d_text["over25"] = [
            '暑いときは汗をかくから、その分水を飲まないとね…',
            '熱帯夜は寝苦しいよね。そんなときは、羊を数えるんだ。',
            "暑いから水分をよく摂って、熱中症に気をつけてね。"
            ]
        self.d_text['w_over30'] = [
            '最近暑い日が続くけど、大丈夫？無理しないでね…',
            '{}も暑いね…。水はこまめに飲むといいんだって。'.format(date),
            "{}も暑いね。また海に行きたいかも…今度はバイクで。".format(date)
            ]
        self.d_text['w_under0'] = [
            '寒い日が続くから、体が温まるものを食べるといいんじゃないかな…',
            'みんなは大丈夫？寒いのにはもう慣れてきた？',
            '{}も寒そうだね。マフラーと手袋を忘れずにね。'.format(date)
            ]
        self.d_text["fine"] = [
            "{}はとてもいい天気になりそう…こんな日にライブしたいなぁ…なんてね。".format(date),
            '天気がいいから外でレッスン？…まあ、悪くないかな…。'
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で一番低いんだって。風邪ひかないように気をつけてね。".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番冷え込むんだって。体を冷やさないようにね。".format(date)
        self.d_text["w_hot_max"] = {
            'term':'kion_max','cases':2,'border':25,
            1 : "{}は急に暑くなるから、体調管理に気をつけてね。".format(date),
            0 : "{}はここ最近で一番暖かいよ。涼しめの服装がいいかも…".format(date)
            }
        self.d_text['w_hot_min'] = {
            'term':'kion_min','cases':2,'border':18,
            1 : "{}はここ一週間で最低気温が一番高いんだって。ちょっと暑いかもね".format(date),
            0 : "{}はここ一週間で最低気温が一番高いんだって。過ごしやすい日になるかな…".format(date)
            }
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            1 : "{}は{}よりも{}度も暑いんだって。涼しい格好の方がいいかもね。".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            0 : "{}は{}よりも{}度も暖かいって。気温差に注意してね。".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いんだって。気温差に気をつけてね。".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いんだって。気温差に気をつけてね。".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低くて、とても冷え込みそうだよ。'.format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低くて、とても冷え込みそうだよ。'.format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text['snow_1-10'] = {
            'term':'am_pm','cases':2,'border':1,
            1 : "{}はさらに雪が積もりそうだよ。また事務所に雪だるまが増えてそう。".format(date),
            0 : '現在の積雪は{}cmだけど、まだまだ積もりそうだね。'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text['snow_1-1'] = {
            'term':'am_pm','cases':2,'border':1,
            0 : '現在の積雪は{}cmだけど、さらに積もりそうだね。'.format(s_data[3][0]),
            1 : "{}の降雪でまた雪が積もるかもだね。".format(date)
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = "{}は雪が降るみたいだから、交通機関の情報にも注意してね。".format(date)
        #雪が降らん＆積雪が十分にある
        self.d_text['snow_0-10'] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmだよ。雪の対策は大丈夫？".format(s_data[3][0]),
            1 : "雪が積もってるみたい。ハナコにも見せてあげようかな。"
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "うっかりして、凍った雪で滑らないようにね。"

        self.d_text['nothing_am']= [
            "うん、それじゃあ今日も一日頑張ろう。",
            'じゃあ、みんな遅刻しないようにね。',
            '夜の天気予報もチェックよろしくね。'
            ]
        self.d_text['nothing_pm']= [
            'ふぅ…じゃあみんな、おやすみなさい。',
            '今日はお疲れ様。夜更かししないようにね。',
            '明日の天気予報もチェックしてね。'
            ]
        self.d_text['special'] = [
            '今年も天気予報をよろしくね…',
            'え…私のチョコ…欲しいの？',
            '私がお雛様なら、お内裏様は…あの人かな…',
            'いつもデレステをプレイしてくれてありがとう…これからもよろしくね。',
            'ハロウィンだからって…そんなに浮かれすぎちゃダメだよ。',
            'いつもモバマスをプレイしてくれてありがとう…これからもよろしくね。',
            '私へのプレゼントは…あるの？'
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

        self.f_text = self.aisatsu+'\n'+self.tenki+self.kion+self.c_text+'\n'+ht

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
    cin = Rin(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは渋谷凛の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
