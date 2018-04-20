import numpy.random as nmr
import datetime as dt
import common_function as cf

class Yuko:
    def __init__(self,am_pm,japan,prediction,cond,s_data):

        self.place = prediction[0]
        self.weather = prediction[2]
        self.weather_id = prediction[3]
        self.kion_max = int(prediction[4][0])
        self.kion_min = int(prediction[4][1])
        self.rain = prediction[6]

        rand_word = ["","の予報"][nmr.randint(2)]
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
            "おはようございます！エスパーユッコこと、堀裕子の天気予報の時間です！",
            "むむむーんっ、今からユッコのさいきっくぱわーで天気を予知しちゃいますよ！",
            'さいきっく〜未来予知っ！明日の天気を予知しちゃいます！'
            ]
        self.goode_box = [
            "さあ、ユッコのサイキック天気予報の時間ですよ。むんっ！",
            "むむむーんっ、今からユッコのさいきっくぱわーで天気を予知しちゃいますよ！",
            'さいきっく〜未来予知っ！明日の天気を予知しちゃいます！'
            ]
        self.special =[
            'ハッピーニューイヤー！新年の天気予報の時間です！',
            'ハッピーバレンタイン！ユッコによる{}の天気予報の時間です！'.format(date),
            [cf.rand_sel(self.goodm_box),cf.rand_sel(self.goode_box)][am_pm],
            'デレステ配信{}周年ですね！天気予報のあとでパーティーしましょう'.format(japan.year-2015),
            'トリックオアトリート！お菓子をくれないと天気を教えてあげませんよっ',
            'モバマス配信{}周年おめでとうございますっ！みんなで祝いましょう！'.format(japan.year-2011),
            'メリークリスマ〜ス！クリスマスも天気予報ですよっ'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度{}です。".format(self.kion_max,self.kion_min,rand_word)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = [
            "{}は嵐…流石の私でも、サイキックパワーで天気を変えることはできません…".format(date),
            'むーーん！、さいきっくてるてる坊主です！{}の雨が止みますように☆'.format(date)
            ]
        self.d_text["rain_123"] = "{}は一日を通して降水確率が{}％を越えそうなので傘が必要ですよ！".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "{}は午前中の降水確率が{}％、午後は{}％です。傘を持って出かけましょう！".format(date,self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％です。雨が降ってなくても傘を持っていきましょう！".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％です。遅くまで外出する人は傘を持っていきましょう！".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％です。出かける時は傘を持っていきましょう！".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差の激しい１日になります。脱ぎ着のしやすい服がオススメですよっ".format(date)
        self.d_text["under10"] = [
            "{}は冷え込むので、暖かい格好で出かけましょう！".format(date),
            "寒くても私にはパイロキネシスがあるから大丈夫です。むんっ！"
            ]
        self.d_text["under0"] = [
            "こんな寒い日は温泉に浸かってサイキックエナジーを蓄えましょう！",
            "超能力者には寒さなんて効きま…ハ…ハクション！"
            ]
        self.d_text['w_under0'] = [
            '今日も寒いですね〜。でも、サイキッカーは風邪をひかないって言いますから！…あれ？違う？',
            'セーターとTシャツをゴシゴシして…はいっ！さいきっく静電気〜',
            "暖房のつけすぎはギルティ！そんな悪者はくらえ、さいきっく・おいろけビーム！！"
            ]
        self.d_text["over30"] = [
            "私の透視にかかればスイカ割りなんて…って、あれっ？割れてない〜！",
            "冷房のつけすぎはギルティ！そんな悪者はくらえ、さいきっく・おいろけビーム！！"
            ]
        self.d_text["over25"] = [
            "私のスプーン、アイスを食べる時も使えるんですよ。便利でしょう！",
            "熱中症には注意です！水をこまめに飲みましょう"
            ]
        self.d_text['w_over30'] = [
            "冷房のつけすぎはギルティ！そんな悪者はくらえ、さいきっく・おいろけビーム！！",
            "私の透視にかかればスイカ割りなんて…って、あれっ？割れてない〜！",
            'これはサイキックですかっ？アイスクリームがどんどん溶けていきます〜'
            ]
        self.d_text["fine"] = [
            "{}はいい天気ですね！さいきっくぱわーを磨くにはもってこいです！".format(date),
            '{}は天気がいいので、サイキックパワーが高まる気がします〜'.format(date)
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で一番低いです。上着はいつもより厚めにしましょう".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番冷え込みますよ。上着はいつもより厚めにしましょう".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はこの一週間で一番暖かいですよ。いつもより薄い服で出かけましょう".format(date),
            1 :"{}はここ最近で一番の暑さですよ。急に暑くなるとサイキックが暴発しそうで…".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いですよ。いつもより涼しい服がいいですよっ".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}は{}よりも{}度も暖かくなります。いつもより薄着にしましょう".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}は{}よりも{}度も暑いです。急な暑さに注意してくださいね".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いですっ。昨日より薄着がいいでしょうっ".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低いですっ。急に寒さに驚いちゃうかも〜'.format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低いですっ。急に寒さに驚いちゃうかも〜'.format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : "さいきっく雪合戦っ！飛べっ雪玉よ、みんなをめがけてー！",
            0 : '今の積雪は{}cmだけど、まだまだ積もりそうですっ！'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : "{}はさらに雪が積もりそうです。雪だるま…作りますか？".format(date),
            0 : '今の積雪は{}cmですね。{}はもっと積もるかも！'.format(s_data[3][0],date)
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = "雪が降るんですか？{}の学校、お休みにならないかなぁ".format(date)
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmです。けっこう積もってますね！".format(s_data[3][0]),
            1 : '雪かきは私のサイキックにお任せあれ！'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "私、池の上を歩いてます！え、それはサイキックじゃなくて凍ってるから？"

        self.d_text['nothing_am']= [
            "twitterだけでなくテレパシーでも届けちゃいますよ。ムムムーン！",
            "次はユッコの特技、スプーン曲げを披露しちゃいますよ…え、時間がない！？",
            "twitterばかり見ているあなたはギルティ！さいきっく・おいろけビームでお仕置きです！",
            ]
        self.d_text['nothing_pm']=[
            "twitterだけでなくテレパシーでも届けちゃいますよ。ムムムーン！",
            "次はユッコの特技、スプーン曲げを披露しちゃいますよ…え、時間がない！？",
            "twitterばかり見ているあなたはギルティ！さいきっく・おいろけビームでお仕置きです！",
            ]
        self.d_text['special'] = [
            '私、初詣はパワースポットにも行きたいですね！',
            'このチョコは私の念を込めて作った特別なチョコなんですよっ',
            'ひな祭りは女の子の健やかな成長を願うお祭り…私のサイキックパワーももっと強く！',
            'デレステ{}周年目指して、もっとサイキックパワーを磨きます！'.format(japan.year-2014),
            'ハロウィン…、日本の盛り上がりがすごくて、アーニャびっくりしました。',
            'モバマス{}周年に向けて、もっと頑張ります！'.format(japan.year-2010),
            'クリスマスプレゼントは…特製のスプーンセットをぜひっ！'
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
    cin = Yuko(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは堀裕子の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list,36,45)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
