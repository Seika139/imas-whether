import numpy.random as nmr
import datetime as dt
import common_function as cf

class Momoka:
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
            "みなさん、櫻井桃華のお送りする天気予報の時間ですわよ。",
            "みなさん、起きてますか？桃華の天気予報の時間ですわよ。",
            "おはようございます、櫻井桃華ですわ。今朝の天気予報の時間ですの。"
            ]
        self.goode_box = [
            "今日もお疲れ様です。わたくしの天気予報を見てくださいまし。",
            'こんばんは、櫻井桃華ですわ。今夜の天気予報の時間ですの。'
            ]
        self.special =[
            'あけましておめでとうございます。今年もよろしくお願い致しますわ',
            'みなさんごきげんよう。今日はバレンタイン、なんだかワクワクしますの',
            'あら、今日は桃の節句ですわね。わたくしにも『桃』が入ってますのよ。',
            'デレステ{}周年ですわね。夜のパーティーがとっても楽しみですの。'.format(japan.year-2015),
            'ハッピーハロウィン！今日ははしゃいでもいいんですのよ♪',
            'モバマス配信から{}周年、振り返ればあっという間ですわね。'.format(japan.year-2011),
            'メリークリスマス！みなさんに幸せな聖夜をお届けしますわ♪'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度ですわ。".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = "{}は荒れた天気になるようですの。不要な外出はお控えくださいまし。".format(date)
        self.d_text["fine"] = [
            "{}はいい天気ですの？それならレッスンの時間までシャボン玉を…".format(date),
            "{}はいい天気になるようですの。お庭でローズヒップティーを嗜むのもいいですわね♪".format(date)
            ]
        self.d_text["rain_123"] = "{}は１日を通して降水確率が{}％を越えるようですの。傘を忘れずにお出かけなさいませ。".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "午前中の降水確率が{}％、午後は{}％ですの。外出時には、傘を持って行ってくださいな。".format(self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％ですの。雨が降ってなくても傘を持っていってくださいな。".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％ですわ。遅くまで外出する人は傘を持っていきなさいませ。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％ですわ。出かける時は傘をお持ちになってくださいな。".format(date,self.rain[2])
        self.d_text["kionsa"] = '{}は気温差の激しい１日になりますの。脱ぎ着のしやすい服装がよろしいですわ。'.format(date)
        self.d_text["under10"] = [
            "{}は寒いですわ。寒さ対策はしっかりしてくださいな。".format(date),
            "子供は風の子ですわ。わたくしは寒くても大丈夫ですの。"
            ]
        self.d_text["under0"] = [
            "寒い時は温かい紅茶で身も心も温めましょう。",
            "こんな寒い日は温かい紅茶が欲しくなりますわね。"
            ]
        self.d_text['w_under0'] = [
            "{}も冷え込みますの。暖かい格好でお出かけなさいまし。".format(date),
            '"みなさん寒い中がんばってらして…私も負けてられませんわ！"'
            ]
        self.d_text["over30"] = [
            "プールで遊ぶのもいいですが、今度は事務所の皆さんと海水浴にも行きたいですわ♪",
            'これが線香花火…大きな花火とは一味違う風情がありますわね。'
            ]
        self.d_text["over25"] = [
            "日焼け肌…お風呂が怖いかも…ヒリヒリしないといいのですけど…",
            "ホースからでる水で虹ができて…ひゃあっ、私にはかけないでくださいましっ…"
            ]
        self.d_text['w_over30'] = [
            "暑い日が続きますわ。熱中症には気をつけてくださいまし。",
            "桃華の水着をお披露目ですわ！ビーチボールで遊びましょう♪",
            'ふぅ、暑いですわね…冷えたお水が、気持ちいい…。氷の入ったアイスティーをいただきたいですわね。'
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で最も低いですわ。薄着では風邪をひきますわよ。".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番寒いですわ。薄着では風邪をひきますわよ。".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はこの一週間で一番暖かいですわ。ポカポカした陽気になるといいのですけど。".format(date),
            1 :"{}はこの一週間で一番の暑さですわ。きっと汗をかくような日になりますの。".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高ですの。普段よりも薄着がいいですわよ。".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}より{}度も暖かくなりますわ。{}とは季節が違いますわよ。".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]),pre_date),
            1 : "{}より{}度も暑くなりますわ。紅茶はホットよりもアイスにしましょう。".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}よりも最低気温が{}度高いのですわ。{}よりも薄着がよろしいですわよ".format(pre_date,cf.rbs(self.kion_min-s_data[1][0]),pre_date)
        self.d_text["y_cold_max"] = '{}よりも最高気温が{}度も低いですわ。紅茶は温かいのがいいですわね。'.format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}よりも最低気温が{}度も低いですわ。服装はちょっと厚着がよろしいですわよ'.format(pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : 'なんて雪景色…。まるでおとぎの国にいるようですわ。',
            0 : '現在の積雪は{}cmですの。今日はさらに雪が積もるようですわ'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : '雪遊び…たまには事務所のみなさんとはしゃぐのもいいかもしれませんわね♪',
            0 : '現在の積雪は{}cmですの。今日も雪が積もるかもしれませんわ。'.format(s_data[3][0],date)
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = '雪が降りますの？そ、そんな…はしゃいでなんかいませんわ！'
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmですわ。雪に足が取られないように気をつけなさいまし。".format(s_data[3][0]),
            1 : '事務所にみんなの雪だるまがありますの。見に来てもいいんですのよ？'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "雪で滑ってしまわないよう注意ですわ！私なら大丈夫ですの。"

        self.d_text['nothing_am']= [
            "寝坊するのはめっ！ですわよ♪",
            "朝食はきちんと食べまして？基本ですわよ。",
            "ほら、もう行かないと遅刻ですわよ！"
            ]
        self.d_text['nothing_pm']=[
            "夜更かしするのはちょっとドキドキしますわ！",
            "ふわぁ…ね、眠くなんかありませんわっ！",
            '夜更かししたら明日起きられない…？そんな子供じゃありませんわよ！',
            "ローズヒップティーは適温で。おぼえてくださいまし♪"
            ]
        self.d_text['special'] = [
            'まあ！きちんと並べたつもりですのに、なんて面白いお顔！うふふっ、これが福笑い…楽しいですわ♪',
            'このわたくしのチョコレートがほしくて？いいですわ。替わりにアナタ方のハートを頂きますわ',
            'まあ、立派なひな壇ですの。可愛いお人形が飾られて…素敵ですわね♪',
            '夜の舞踏会は賑やかに踊りましょう。仁奈さんと薫さんも一緒に！高くJumpです♪',
            'トリックオアトリート！わたくしだってイタズラすることくらいあるんですのよ♪',
            '記念日を祝うパーティー、気品ある振る舞いをしてみせますわ。',
            'クリスマスツリーのトップスターには、『希望の光』って意味があるそうですわ。知っていまして？'
            ]
        self.d_text['hanami'] = [
            "ねえお花見しよ♪\nふふ、ドキドキしまして？",
            "まゆさんのお弁当が素晴らしくて…わたくしからはお茶でおもてなしですの。",
            '杏さんたらそんな恰好で食べて…お餅を喉に引っ掛けてしまいますわよ？',
            '杏さんに頂いたあんず飴…忘れられない思い出ですわ♪',
            '桜のように舞い踊りますわ。パーリラパリラハイ♪'
            ]
        self.d_text['rose'] = '本日6月2日はローズの日ですの。わたくしの家の庭でもたくさん咲いてますのよ。'


        if cond[1] == 0:
            self.c_text = cf.special_day(japan,self.d_text['special'])
            if self.c_text == None:
                if japan.month==4 and japan.day<=10: self.c_text = cf.rand_sel(self.d_text['hanami'])
                elif japan.month==3 and japan.day>=25: self.c_text = cf.rand_sel(self.d_text['hanami'])
                elif japan.month==6 and japan.day==2: self.c_text = cf.rand_sel(self.d_text['rose'])
                elif am_pm == 0: self.c_text = cf.rand_sel(self.d_text['nothing_am'])
                else: self.c_text = cf.rand_sel(self.d_text['nothing_pm'])
        elif cond[1]<=10 and japan.month== 4 and japan.day<=10: self.c_text = cf.rand_sel(self.d_text['hanami'])
        elif cond[1]<=10 and japan.month== 3 and japan.day>=25: self.c_text = cf.rand_sel(self.d_text['hanami'])
        elif cond[1]<=10 and japan.month== 6 and japan.day==2: self.c_text = cf.rand_sel(self.d_text['rose'])
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
    cin = Momoka(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは櫻井桃華の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
