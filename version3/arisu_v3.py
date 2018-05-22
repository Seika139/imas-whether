import numpy.random as nmr
import datetime as dt
import common_function as cf

class Arisu:
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
            "{}時なりました。橘ありすの天気予報の時間です。".format(japan.hour%12),
            "みなさん、起きてますか？橘ありすの天気予報の時間です。",
            "おはようございます、今朝の天気予報は橘ありすがお送りします。",
            'おはようございます。橘ありすのお送りする天気予報の時間です。'
            ]
        self.goode_box = [
            "{}時なりました。橘ありすの天気予報の時間です。".format(japan.hour%12),
            'こんばんは、今夜の天気予報は橘ありすがお送りします。',
            'お仕事お疲れ様です。天気予報を見て明日に備えましょう。',
            'こんばんは。橘ありすのお送りする天気予報の時間です。'
            ]
        self.special =[
            '新年おめでとうございます。みなさん年賀状は書きましたか？',
            'こんにちは…きょ、今日はバレンタインですね。私は平常運転ですよ…',
            [cf.rand_sel(self.goodm_box),cf.rand_sel(self.goode_box)][am_pm],
            'デレステ{}周年おめでとうございます。今後もよろしくお願いしますね'.format(japan.year-2015),
            'ハロウィンの時期ですが、みなさんはハロウィンの由来はご存知ですか？',
            'モバマス{}周年ですね。素敵な記念日にしましょう。'.format(japan.year-2011),
            'メリークリスマス！デコレーションケーキで甘い聖夜を過ごしませんか？'
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
        self.d_text["storm"] = "{}の天気は大荒れのようですが、レッスンならできます！".format(date)
        self.d_text["fine"] = [
            "{}はいい天気になるようですが、どこかのプロデューサーみたいに浮かれてちゃダメですよ！".format(date),
            "{}はいい天気みたいです。桃華さんに教わった淹れ方で紅茶を飲んでみようかな…".format(date)
            ]
        self.d_text["rain_123"] = "{}は１日を通して降水確率が{}％を越えるようです。傘を忘れずに持っていきましょう。".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "午前中の降水確率が{}％、午後は{}％です。外出時は、傘を持って行ってください。".format(self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％です。雨が降ってなくても傘を持っていくのがいいでしょう。".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％です。遅くまで外出する人は傘を持っていきましょう。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％です。出かける時は傘が必要です。".format(date,self.rain[2])
        self.d_text["kionsa"] = '{}は気温差の激しい１日になります。脱ぎ着がしやすい服装がいいですね。'.format(date)
        self.d_text["under10"] = [
            "{}は冷え込むので、暖かい格好で出かけましょう。".format(date),
            "寒い季節はイチゴが美味しいですね。まあ、いつでも美味しいんですけど…"
            ]
        self.d_text["under0"] = [
            "寒いのは苦手ですけど、プロとしてお仕事はちゃんとこなしますよ！",
            "最近はホットコーヒーにチャレンジしてるんです。ブラックはまだ飲めませんが…"
            ]
        self.d_text['w_under0'] = [
            "{}も冷え込みます。暖かい格好で出かけてください".format(date),
            '寒い日が続きますね。たまには長風呂で体を芯から温めてはどうでしょう。'
            ]
        self.d_text["over30"] = [
            "川の水がひんやりとして気持ちいい…水面に映る花火も綺麗ですね。",
            'このぐらいの暑さでへばってるようじゃまだまだですよ…もぅ。'
            ]
        self.d_text["over25"] = [
            "牧場でいただくアイスは絶品です。イチゴとミルクのアイス、皆さんも食べてみてください！",
            "ラムネは夏の風物詩と言うそうですね…桃華さん、開け方分かりますか…？"
            ]
        self.d_text['w_over30'] = [
            "屋外のステージは日焼け止めを塗る面積が大きくて…、別に手伝って欲しいわけではないです！",
            "出店で買い食いするのは卒業しました。でも、たまにはいいかな…",
            '暑い日が続きますね。うちのプロデューサーみたいにバテてるようじゃダメですよ！'
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で最も低いです。寒さを考慮した服装にしましょう。".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番寒いですよ。薄着で風邪をひかないでくださいね".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はこの一週間で一番暖かいです。普段より薄着がいいでしょう。".format(date),
            1 :"{}はこの一週間で一番の暑さ、半袖でも過ごせるような日になりそうです。".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いです。上着はいつもより薄いもので大丈夫ですよ".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}より{}度も暖かくなります。{}よりも薄着がいいでしょう。".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]),pre_date),
            1 : "{}より{}度も暑くなります。急な暑さに注意してくださいね。".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}よりも最低気温が{}度も高くなります。{}よりも薄着がいいでしょう".format(pre_date,cf.rbs(self.kion_min-s_data[1][0]),pre_date)
        self.d_text["y_cold_max"] = '{}よりも最高気温が{}度も低いので急な寒さに気をつけてください。'.format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}よりも最低気温が{}度も低いので厚着を心がけてください。'.format(pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : '事務所のみんなは屋上で雪だるまを作ってます。わ、私は行きませんよ…',
            0 : '現在の積雪は{}cmです。今日の雪でさらに積もる予想です。'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : 'ちゃんと雪を落としてから中に入ってくださいよ、もう。',
            0 : '現在の積雪は{}cmです。今日もさらに積もると思われます。'.format(s_data[3][0])
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = 'ゆ、雪ですか…？私は子供みたいにはしゃぎませんよ…'
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmです。車で出かける人は気をつけてくださいね。".format(s_data[3][0]),
            1 : '雪の結晶っていろんな形があるんですね！不思議な形ですよね。'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = [
            "油断してると氷で足を滑らせますよ。私のプロデューサーみたいに…",
            '解けた雪の水はどこに行くんですか？あとで調べてみます。'
            ]

        self.d_text['nothing_am']= [
            'で、ですからありすではなく、橘と呼んでください！もう…',
            '今回はクールタチバナ、見せられましたか？',
            '遅刻するのはプロのすることじゃありませんよ。まだ朝ごはん食べてるんですか？'
            ]
        self.d_text['nothing_pm']=[
            "おいしいだけでなく美しい、私が目指すのはイチゴのようなアイドル…",
            "奏さんも文香さんとのランチ。なんだか大人になった気分…コーヒーだって飲めますよ…",
            'twitterでのリサーチは任せてください。',
            "毎月22日はショートケーキの日です。なぜなら上にイチゴ(15)が乗ってますからね。"
            ]
        self.d_text['special'] = [
            '今年の目標は、もっと身長を伸ばすことですね…',
            '仕事なのは分かってますけど…とてもドキドキしますね。',
            'ひな祭りですか？わ、私は子供ではないので大丈夫です…',
            '夜のパーティーは子供も参加していいんですよね？ねぇ？',
            '私はハロウィンの由来知ってますよ。ちゃんと調べましたからね。',
            'いつも支えてくださる皆さんには感謝です。私も気を引き締めて頑張ります。',
            'サンタさんに、どんなプレゼントお願いしたかって…？ な、内緒です！'
            ]
        self.d_text['strawberry'] = [
            "1月15日はいちごの日です。是非、いちごを食べてくださいね！",
            "1月15日はいちごの日です。みなさん、いちごパスタはいかがですか？",
            '15日のいちごの日に向けて、いちごパスタの試作会です。味見してくれますか？'
            ]


        if cond[1] == 0:
            self.c_text = cf.special_day(japan,self.d_text['special'])
            if self.c_text == None:
                if japan.month==1 and 12<=japan.day<=15: self.c_text = cf.rand_sel(self.d_text['strawberry'])
                elif am_pm == 0: self.c_text = cf.rand_sel(self.d_text['nothing_am'])
                else: self.c_text = cf.rand_sel(self.d_text['nothing_pm'])
        elif cond[1]<=10 and japan.month==1 and 11<japan.day<16: self.c_text = cf.rand_sel(self.d_text['strawberry'])
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
    cin = Arisu(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは橘ありすの天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
