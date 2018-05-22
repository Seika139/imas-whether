import numpy.random as nmr
import datetime as dt
import common_function as cf

class Mio:
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
            greet = "おっはよ〜"
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"
            greet = "こんばんは〜"

        """ 1. 挨拶 """

        self.goodm_box = [
            "みんな、おっはよ〜！本田未央の天気予報の時間だよ☆",
            "さあ、みんな起きた起きた！天気予報の時間だぞっ。",
            "やっほー、みんな朝だぞ☆天気予報をチェックして出かけよう！"
        ]
        self.goode_box = [
            "こんばんは、本田未央だよ☆ みんなに明日の天気を教えてあげよう！",
            "デレッパー！…じゃなかった。こんばんは、本田未央の天気予報だよ。",
            "こんばんは、本田未央です！明日の天気予報の時間だよ☆"
        ]
        self.special =[
            'ハッピーニューいえ〜い！！今年の天気予報もよろしくね！',
            'ハッピーバレンタイン！未央ちゃんの天気予報だぞ〜',
            '{}、今日は桃の節句、ひな祭りだね！'.format(greet),
            'デレステ配信{}周年、おめでとう！パチパチパチー'.format(japan.year-2015),
            'ハッピーハロウィン！{}の天気予報の時間だよ！'.format(date),
            'モバマス配信{}周年おめでとう！ほらみんな、クラッカーの準備！'.format(japan.year-2011),
            'メリークリスマス！未央ちゃんの天気予報だよ〜'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報だよ！".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = [
            "{}は大雨だけど、雨にも負けず！がんばろー！".format(date),
            "うーん、{}は天気が悪いみたい。お出かけしたいのになぁ".format(date)
            ]
        self.d_text["rain_123"] = "{}は1日を通じて降水確率が{}％を越えそうだから、出かけるときは傘を忘れずにね！".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "{}は午前中の降水確率が{}％、午後は{}％となる見込みだよっ。傘を忘れずに持っていってね！".format(date,self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "{}は午後の降水確率が{}％、夜は{}％だから、朝降ってなくても傘を持っていこう！".format(date,self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％だよ。夕方から雨が降るかもだねっ。帰りが遅い人は傘を忘れずにー。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％だよ。出かける人は傘を持って行こう！".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差が激しいよ。脱ぎ着のしやすい服がいいかもね☆".format(date)
        self.d_text["under10"] = [
            "{}も寒いけど、元気出していってみよ〜！".format(date),
            '冬場に外出するときは、ネクタイだけじゃなくてマフラーも巻いてねっ'
            ]
        self.d_text["under0"] = [
            '寒～い外で遊んだあとは、あったか～い部屋でアイスを食べる…それが冬っ！',
            'いやぁ、こんな日はみんなで鍋パがしたいなぁ'
            ]
        self.d_text["over30"] = [
            '夏は海だ！セクシー担当未央ちゃんの水着がみたい？…え、セクシー担当じゃない？',
            '三ツ星アイドルを目指す私にはこんな暑さ負けられないぜっ！'
            ]
        self.d_text["over25"] = [
            'ちゃ〜んと、水分とってるかな？',
            '夜も暑くてエアコンがないと寝れないよ〜'
            ]
        self.d_text['w_over30'] = [
            '今日も明日も暑さに負けず、がんばろ〜！',
            '今度のグラビア撮影に備えて運動しなきゃ！',
            '{}も暑いみたいだよ。水分補給を忘れずに！'.format(date)
            ]
        self.d_text['w_under0'] = [
            '子供は風の子！寒くても体を動かせば大丈夫！',
            '寒い日が続くけど、みんなは元気？私はもちろん元気元気！'
            ]
        self.d_text["fine"] = [
            "{}は晴れていい天気になりそうだよ！なんだかいいことが起こりそうー！".format(date),
            '{}はとってもいい天気！ライブ日和だね☆'.format(date)
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で一番低いんだって。寒そうだね".format(date)
        self.d_text["w_cold_min"] = "{}はここ最近で一番冷え込むみたいだよ。体を壊さないように注意！".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はここ最近で一番暖かいみたい。重ね着は１枚少なめに〜".format(date),
            1 :"{}はここ最近で一番の暑さだよ！熱中症には気をつけてね".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高くなるって。少し涼しい服装がいいかも。".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}は{}よりも{}度も暖かいみたいだよ。急な暖かさに驚いちゃうかも".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}は{}よりも{}度も暑いみたい。急な暑さにビックリしないようにね☆".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いんだって。ちょっと薄着がいいかも。".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低いよ。体を壊さないようにね☆'.format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低くて、結構寒そう〜'.format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = [
            "{}はさらに雪が積もりそう。スキーで学校までいけちゃうかも！".format(date),
            "一級カマクラ建築士の未央ちゃんによると…ふむ、あれはいい仕事ですな",
            '真っ白な世界を、未央ちゃん色に染めちゃおー！'
            ]
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
        'term':'am_pm','cases':2,'border':1,
        1 : "{}はさらに雪が積もりそう！みんなで雪合戦だ！".format(date),
        0 : 'ただいまの積雪は{}cm。{}はもっと積もるかも！'.format(s_data[3][0],date)
        }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = "雪が降るのは冬の間だけっ。楽しまなかったら、もったいないよねっ☆"
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cm！スノーブーツがいいかもね。".format(s_data[3][0]),
            1 : "外を見ればほら、雪だるまがたくさん！"
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "解けかけの雪は滑りやすいから注意だよ☆"

        self.d_text['nothing_am']= [
            "それじゃあみんな、行ってらっしゃ〜い！",
            'よーし、今日も一日がんばろー！',
            '夜の天気予報もチェックよろしくー！'
            ]
        self.d_text['nothing_pm']=[
            'それじゃあみんな、おやすみなさ〜い',
            'さあさあ、良い子のみんなは寝る時間だぞ〜！',
            '明日の天気予報もチェックよろしくー！'
            ]
        self.d_text['special'] = [
            '私、これからもいーっぱい頑張るから今年もよろしくね☆',
            'いつものお礼に、バレンタインチョコ！はい、どうぞ！',
            'えーっと、お内裏様とお雛様と、五人囃子に…あとなんだっけ？',
            'これからもデレステをよろしくね！',
            'トリックオアトリート！未央ちゃんがイタズラしちゃうぞ☆',
            'これからもモバマスをよろしくね！',
            '未央ちゃんへのプレゼントは何かな？何かな？'
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
    cin = Mio(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは本田未央の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
