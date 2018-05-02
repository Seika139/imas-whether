import numpy.random as nmr
import datetime as dt
import common_function as cf

class Miku:
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
            greet = "おはようございますっ！"
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"
            greet = "こんばんはー"

        """ 1. 挨拶 """

        self.goodm_box = [
            "おっはよ〜！{}の天気予報をこのみくがお送りするにゃ！".format(date),
            'ふわぁ、おはよー…って、もう天気予報始まってるじゃん！',
            "みんな、おはよ〜！みくのにゃんにゃん天気予報始まるよー",
            'グッドモーニングだにゃっ。今日も天気予報を見て一日がんばろー！'
            ]
        self.goode_box = [
            "今日もお仕事お疲れ様♪みくの天気予報の時間にゃ",
            "こんばんにゃあ！{}の天気予報はこのみくがお送りするにゃ！".format(date),
            "みんな、お疲れ〜！みくのにゃんにゃん天気予報の時間だよ〜"
            ]
        self.special =[
            'あけましておめでとうにゃ！今年も天気予報よろしくなのにゃ〜！',
            'ハッピーバレンタイン！みくの{}の天気予報の時間にゃ'.format(date),
            [cf.rand_sel(self.goodm_box),cf.rand_sel(self.goode_box)][am_pm],
            'デレステ配信{}周年おめでとう！アニバーサリーなんだにゃあ'.format(japan.year-2015),
            'ハッピーハロウィン〜。{}の天気予報の時間だにゃ'.format(date),
            'モバマス配信{}周年おめでとうー！みんなでお祝いするにゃあ'.format(japan.year-2011),
            'メリークリスマ〜ス！今年もクリスマスがやってきたのにゃ〜'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度だにゃ。".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = '大雨だと尻尾が濡れちゃうから困るにゃ〜'
        self.d_text["rain_123"] = "{}は一日中降水確率が{}％を越えそうだから傘が必要だにゃ。".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "{}は午前中の降水確率が{}％、午後は{}％だって…傘を忘れずに持っていくにゃあ".format(date,self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％だから、雨が降ってなくても、傘を持っていくにゃ！".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％。夕方から雨が降りそうだから傘を持って出かけるにゃあ。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％だよ。出かけるときは傘を持っていくといくにゃあ".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差の激しい１日になるから服装に注意するにゃ！".format(date)
        self.d_text["under10"] = [
            "フゥー…寒いにゃあ。みくも毛皮があれば〜",
            'ネコチャンを抱くと暖かいんだけどにゃ〜'
            ]
        self.d_text["under0"] = [
            "{}度は寒すぎるにゃ〜。鳥肌、いや、猫肌が立つにゃ！".format(self.kion_min),
            "{}は寒いよ〜。猫カフェでゆっくり温まりたいにゃあ".format(date)
            ]
        self.d_text['w_under0'] = [
            '今日も寒いねー、ほんとは…お布団でゴロゴロしたいけど我慢我慢！',
            'あったかいお茶は好きだけど、みくは猫舌で…その…',
            '寒い日にはたい焼きなんてどう？ほら、美味しそうでしょ〜'
            ]
        self.d_text["over30"] = [
            "あったかいのは好きだけど、{}は暑すぎるにゃあ".format(date),
            'ほら、暑い日は海に行くよ！セクシーなみくの水着と猫耳を見て欲しいのにゃ'
            ]
        self.d_text["over25"] = [
            "にゃ〜…暑いよ〜お水が欲しいにゃあ",
            "暑いからネコちゃんはみんな日陰でお昼寝してるにゃあ"
            ]
        self.d_text['w_over30'] = [
            "今日も暑いねー、みんな水分補給を忘れずにね！",
            "お水飲みすぎちゃった。だって暑いんだもん！",
            '今日も水着回にゃ！みんなはどの水着が好き？'
            ]
        self.d_text["fine"] = [
            '天気のいい日は外にいくの。ひなたぼっこして〜お昼寝して〜',
            '{}はいい天気、外のイベントにはぴったりにゃ'.format(date),
            'うーん、いい天気だにゃあ…ムニャムニャ…\nハッ！ね、寝てないもん！'
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がこの一週間で一番低いんだって、ちょっと厚着するにゃ".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番寒いんだって。あったかくして出かけるにゃ".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はこの一週間で一番暖かいって。いつもより薄い服装がいいにゃ".format(date),
            1 :"{}はこの一週間で一番の暑さだにゃ。急に暑いから気をつけてにゃ！".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いんだって。いつもより涼しい服装がいいにゃ".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}は{}よりも{}度暖かくなるから昨日より薄着にするといいにゃ".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}は{}より{}度も暑いのにゃ。急な暑さに注意してにゃ".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いって。{}より薄着にするにゃあ".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]),pre_date)
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低いのにゃ。急に寒さに鳥肌、いや猫肌が立つにゃ〜'.format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低いのにゃ。急に寒さに鳥肌、いや猫肌が立つにゃ〜'.format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : "雪やこんこん♪雪の日、ネコチャンはこたつで丸くなるにゃ〜",
            0 : '今の積雪は{}cmだけど、今日も積もりそうだにゃあ'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : "{}はさらに雪が積もりそうだにゃ。みんな、雪対策は大丈夫？".format(date),
            0 : '今の積雪は{}cmだにゃ。今日はもっと積もるかも！'.format(s_data[3][0])
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = '雪でいつもの街並みがガラッと模様替えにゃあ'
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmだよ。雪に穴を開けて歩くにゃあ".format(s_data[3][0]),
            1 : 'こんなに積もってるなんて…雪に足が取られるにゃあ'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "氷に滑ってと危ないにゃ、歩くときはネコみたいにそーっと…"

        self.d_text['nothing_am']= [
            "今日もお仕事頑張るにゃ〜！",
            "それじゃあみんな、行ってらっしゃ〜い！",
            "ちょっと！お魚の入ってるお弁当はダメって言ったにゃ〜！！"
            ]
        self.d_text['nothing_pm']=[
            "にゃふふ♪今日の猫耳もイケてるにゃ！",
            "いいねをしてくれたみんなから抽選でみくの猫耳をプレゼント！え、勝手にやっちゃだめ？",
            "今日もお仕事お疲れ様♪みんな、お休みなさいなのにゃ"
            ]
        self.d_text['special'] = [
            '今年も天気予報をよろしくなのにゃあ',
            'こ、これは…あ、そのっ…チョコを渡す練習だにゃ…',
            [cf.rand_sel(self.d_text['nothing_am']),cf.rand_sel(self.d_text['nothing_pm'])][am_pm],
            'ノンストップ・アイドルなのにゃー！みくは仲間とともに未来を目指すの！',
            'トリックオアトリート！ネコチャンはイタズラ好きなのにゃ！',
            'メモリアルな日には昔のことを思い出すにゃ。みくがまだ子猫だった頃のこととか…',
            'クリスマスプレゼントは…新しい猫耳が欲しいにゃあ'
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
    cin = Miku(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは前川みくの天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
