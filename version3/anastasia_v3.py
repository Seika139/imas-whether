import numpy.random as nmr
import datetime as dt
import common_function as cf

class Anastasia:
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
            greet = "おはようございます"
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"
            greet = "こんばんは"

        """ 1. 挨拶 """

        self.goodm_box = [
            "ドーブラエ ウートラ！おはようございます。アーニャの天気予報ですよ",
            "プラグノス　パゴーダ…今日の天気予報はアーニャの番ですよ。"
            ]
        self.goode_box = [
            "ドーブルイ　ヴィエーチル！こんばんは。アーニャの天気予報のですよ",
            "プラグノス　パゴーダ…今夜の天気予報はアーニャの番ですよ。",
            'プリヴェート♪皆さん、今日はどんな１日でしたか？'
            ]
        self.special =[
            'ス ノーヴィム ゴーダム！あけましておめでとうございます！',
            '{}。今日はバレンタインですね。'.format(greet),
            '{}、アーニャの天気予報、見てくれますか？'.format(greet),
            '9月3日でデレステ配信{}周年ですね。おめでとうございます'.format(japan.year-2015),
            '{}、アーニャの天気予報、見てくれますか？'.format(greet),
            '11月28日でモバマス配信{}周年ですね。おめでとうございます'.format(japan.year-2011),
            'ス ラジュヂストヴォム…。アー、メリークリスマス…ですよ'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度です。".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = "雨も風も強いです。日本の台風は怖い…ですね。"
        self.d_text["rain_123"] = "{}は一日中降水確率が{}％を越えますね。ゾーンチク…傘を持っていきましょう。".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "午前中の降水確率が{}％、午後は{}％です。ゾーンチク…傘を持って出かけましょう。".format(self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％です。ゾーンチク…傘を持って出かけましょう。".format(date,self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％。夕方から雨が降りそうですよ。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％です。ゾーンチク…傘を持っていきましょう。".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差が激しいです。体を壊さないように気をつけましょう".format(date)
        self.d_text["under10"] = [
            "寒いときはバリトー…コートが必要ですね。",
            "ロシア人がみんな寒い時にウォッカを飲むわけじゃないんですよ。"
            ]
        self.d_text["under0"] = [
            "ロシアほどじゃないですが、日本も寒いですね。",
            '寒い夜はズヴェズダ…星が綺麗に見えますね♪'
            ]
        self.d_text["over30"] = [
            "日本の夏はジメジメ？してます。熱中症に気をつけてくださいね。",
            "アーニャ暑いの苦手です…いっぱいお水を飲みましょう。"
            ]
        self.d_text["over25"] = [
            "日本の夏はジメジメ？してます。熱中症に気をつけてくださいね。",
            "アーニャ暑いの苦手です…いっぱいお水を飲みましょう。"
            ]
        self.d_text['w_over30'] = [
            "アーニャ暑いの苦手です…いっぱいお水を飲みましょう。",
            "アーニャは雪国育ちなので…暑いのは大変です。",
            "寒い国でもアイスはあります。温かいところで食べるの美味しいですから"
            ]
        self.d_text['w_under0'] = [
            'みんな、寒いですか？私のグランマの所はもっと寒いですよ。',
            'アーニャ、寒いのは慣れっこです。みんなは大丈夫…ですか？'
            ]
        self.d_text["fine"] = "{}は気持ちのよい日、になりそうです。".format(date)
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で一番低いです。寒いかも…ですよ。".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番冷え込みます。風邪をひかないでくださいね。".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はここ最近で一番暖かいですよ。いつもより涼しい服…を着ましょう".format(date),
            1 :"{}はここ最近で一番の暑さです。アーニャ、暑いのはちょっと困ります。".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いですよ。いつもより涼しい服…を着ましょう".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}は{}よりも{}度も暖かいです。少し薄着にしましょう。".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}は{}よりも{}度も暑いです。急な暑さに気をつけてくださいね".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いですよ。少し薄着がいいかも…です。".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低いですよ。少し厚着がいいかも…です。'.format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低いですよ。急に寒くなるので注意…です'.format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = [
            "{}はさらに雪が積もりそうですよ。でもグランマのところはもっと積もってますよ".format(date),
            "日本でもこんなに雪が積もるんですね…。美しいです",
            ]
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
        'term':'am_pm','cases':2,'border':1,
        1 : "{}はさらに雪が積もりそうです。雪だるま…作りますか？".format(date),
        0 : '現在の積雪は{}cmです。{}はもっと積もるかも…ですよ'.format(s_data[3][0],date)
        }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = "ダー、雪は冬のマギヤ、魔法…ですね"
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmです。ちゃんと手袋してくださいね。".format(s_data[3][0]),
            1 : '雪が積もってますね。交通情報も雪の影響がないか確認しましょう'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "みんなのところは雪、積もってますか？ブーツで出かけましょう"

        self.d_text['nothing_am']= [
            "みんな、ダスヴィダーニャ！行ってらっしゃい。",
            "ダー。天気予報…日本語の練習になりますね。",
            '夜の天気予報もみてくださいね♪'
            ]
        self.d_text['nothing_pm']=[
            'スパコーイナイ　ノーチ…おやすみなさい、です。',
            "ダー。天気予報…日本語の練習になりますね。",
            '明日の天気予報もみてくださいね♪'
            ]
        self.d_text['special'] = [
            'アーニャ、初詣…に行きたいですね。今年も良い一年になりますように…',
            'ロシアではバレンタインカードを送ったりもするんですよ。',
            'ひな祭り…日本の女の子のお祭りですね。ハラショー♪',
            'これからもデレステをプレイしてくださいね',
            'ハロウィン…、日本の盛り上がりがすごくて、アーニャびっくりしました。',
            'これからもモバマスをプレイしてくださいね',
            'クリスマス…ナジェージタ、希望が叶う日ですよ。'
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
    cin = Anastasia(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールはアナスタシアの天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
