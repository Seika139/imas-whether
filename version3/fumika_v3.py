import numpy.random as nmr
import datetime as dt
import common_function as cf

class Fumika:
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
            greet = "…おはようございます"
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"
            greet = "…こんばんは"

        """ 1. 挨拶 """

        self.goodm_box = [
            "あ、あの、…鷺沢文香のお送りする天気予報の時間です…",
            "…おはようございます、鷺沢文香です。今日の天気予報をお伝えしますね…"
            ]
        self.goode_box = [
            "{}時なりました…鷺沢文香のお送りする天気予報の時間です…".format(japan.hour%12),
            "…こんばんは、鷺沢文香です。明日の天気予報をお伝えしますね…"
            ]
        self.special =[
            '謹賀新年…新たな年の始まりを祝いましょう…',
            'バレンタイン…緊張しますね…。今まで縁がなかったことですから…',
            [cf.rand_sel(self.goodm_box),cf.rand_sel(self.goode_box)][am_pm],
            'デレステ{}周年、私のことも物語に刻まれたと思うと…光栄です…'.format(japan.year-2015),
            'ハロウィンですね…本来は日本のお祭りではないのに大変な盛り上がりで…',
            'モバマス配信{}周年…記念日はやはり特別な思いが湧いてきます…'.format(japan.year-2011),
            'クリスマス…街のイルミネーションが綺麗ですね…'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None: self.aisatsu = cf.rand_sel(self.goode_box) if am_pm else cf.rand_sel(self.goodm_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」…".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報です…".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = "{}は荒れた天気の予報で…。晴耕雨読と言いますので、家で読書はいかがでしょうか…".format(date)
        self.d_text["fine"] = [
            "{}はいい天気になるようで…。たまには外に出て日差しを浴びるのも…".format(date),
            ]
        self.d_text["rain_123"] = "…{}は１日を通して降水確率が{}％を越えるようです。その…傘を忘れずにお出かけください…".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "午前中の降水確率が{}％…午後は{}％です。その…、雨具が必要ですよ…".format(self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "…午後の降水確率が{}％、夜は{}％です…。雨が降ってなくても傘を持っていってください…".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "…{}は夜の降水確率が{}％です。その…遅くまで外出する人は傘をお持ちに…".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％ですので…、出かける時は傘をお持ちください…".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差の激しい１日になるようですので…。脱ぎ着のしやすい服装がよろしいかと…".format(date)
        self.d_text["under10"] = [
            '体を冷やして良いことはありません…マフラーなどをされてはいかがでしょう…',
            '寒くなりますので…温かいお茶はいかがですか…？'
            ]
        self.d_text["under0"] = [
            '最近は工芸茶に興味があって…冷えた体を温めてくれます…',
            '暖炉のある書斎で読書ができれば文句無しですね……'
            ]
        self.d_text['w_under0'] = [
            "冬来たりなば春遠からじ…と言います…。今は寒さに耐えましょう…",
            '地元は長野なので…寒いのは慣れてるつもりなのですが…やっぱり寒いですね……'
            ]
        self.d_text["over30"] = [
            "…外は暑いですが、部屋の中は涼しくて…快適に読書ができます…",
            '…昔の私ならきっと、水着で海に来ることなど、なかったでしょう…',
            '…もしもの話ではあるのですが…私が溺れたら、人命救助を、お願いします…'
            ]
        self.d_text["over25"] = [
            "ナイトプール…美波さんは泳ぎが達者で…私に教えていただけませんか…？",
            '…暑いですね。貧血になりそうです。皆さんもご注意を……'
            ]
        self.d_text['w_over30'] = [
            'そんな…私は運動は苦手なので海水浴は…でもお仕事なら…仕方ありません…',
            '強い日差し…クラクラします…。ちょっと日陰で休んでもいいですか…？'
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で最も低いです…急な寒さに気をつけてください…".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番寒いです…体を冷やさないようにしてくださいね…".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はこれまでの７日間で一番暖かいです…いつもより涼しい格好が良いかと…".format(date),
            1 :"{}はこの一週間で一番の暑さ…私はちょっと耐えられなさそうです…".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いです…寒がりの私でも過ごしやすそうです…".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}より{}度も暖かくなります…{}よりも薄着がいいでしょう。".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]),pre_date),
            1 : "{}より{}度も暑いので…水分補給は忘れずに……。".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}よりも最低気温が{}度も高くなります…急な暑さにはご注意ください…".format(pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}よりも最高気温が{}度も低いです…{}よりも厚着がいいでしょう…'.format(pre_date,cf.rbs(self.kion_max-s_data[0][0]),pre_date)
        self.d_text["y_cold_min"] = '{}よりも最低気温が{}度も低いので…暖かい格好が良いかと……'.format(pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : 'こんなに雪が積もるなんて…幻想的な風景ですね……',
            0 : '現在の積雪は{}cmですが…今日はさらに積もると思われます……'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : '今まで雪の日は屋内で読書をしていたのですが…アイドルになってからはそうはいかないようで…',
            0 : '現在の積雪は{}cmです…今日はさらに積もるかもしれないです…'.format(s_data[3][0])
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = [
        '蛍雪の功…？…いえ、私は読書が好きなだけで……',
        '…雪は普段の街並みを新鮮な姿に変えてくれます…私もイメチェン？…ですか…？'
        ]
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmです…交通機関の情報も確認しましょう…".format(s_data[3][0]),
            1 : '雪は豊年の瑞と言います…成功の影には努力が隠されているという事でしょうか……'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = [
            '雪道は歩きづらいですから…十分気をつけてくださいね…',
            '氷は滑りやすいですので気をつけてください…受験生の方は…特に……'
            ]

        self.d_text['nothing_am']= [
            "春眠暁を覚えずとは言うものの、朝はいつでも眠いもので…",
            "一日の計は朝にあり…と、早起きして良い一日を…",
            "…あ、お勧めの本があれば、お教えください。ジャンルは…そうですね……",
            '奏さんの言われるがままに試着してしまったのですが…いかがですが…？'
            ]
        self.d_text['nothing_pm']=[
            "……ファッション雑誌ですか？…普段は読みませんが…これも勉強ですね…",
            "天気予報…明日もチェックしてくださいね…",
            '夜更かしは体に良くありませんが…夜の読書は捗るので…',
            '時を超えて受け継がれる名作のような…私もそんなアイドルになれるでしょうか…'
            ]
        self.d_text['special'] = [
            '元日と元旦…使い方を間違えている人が多いような気がします…気にし過ぎ…ですか？',
            '…男性を誘うのは慣れてなくて、その、ええと…チョコを受け取ってくれません…か…',
            [cf.rand_sel(self.d_text['nothing_am']),cf.rand_sel(self.d_text['nothing_pm'])][am_pm],
            'こんなドレスを着るようになったのはアイドルになってからで…まるでイリュージョンですね…',
            'イタズラは…その、困ります…。お菓子で許してください…。',
            '…この節目を迎えても、私たちの道は続きます。…物語の新しい章が幕を開けるのですね…',
            'プレゼントですか？……やはり私は本がいいですね。年末は読書をして過ごすので…'
            ]


        if cond[1] == 0:
            self.c_text = cf.special_day(japan,self.d_text['special'])
            if self.c_text == None: self.c_text=cf.rand_sel(self.d_text['nothing_pm']) if am_pm else cf.rand_sel(self.d_text['nothing_am'])
        elif type(self.d_text[cond[0]])==list: self.c_text = cf.rand_sel(self.d_text[cond[0]])
        elif type(self.d_text[cond[0]])==dict:
            x = self.d_text[cond[0]]
            if x['term'] == 'kion_max': elemnt = self.kion_max
            elif x['term'] == 'kion_min': elemnt = self.kion_min
            elif x['term'] == 'am_pm': elemnt = am_pm
            self.c_text = x[1] if element >= x['border'] else x[0]
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
    cin = Fumika(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは鷺沢文香の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list,35,46)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
