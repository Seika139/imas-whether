import numpy.random as nmr
import datetime as dt
import common_function as cf

class Anzu:
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
            greet = "おはよー"
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"
            greet = "こんばんは"

        """ 1. 挨拶 """

        self.goodm_box = [
            "えー今日の天気予報、杏の番なの？？しょーがないな…",
            "みんな、だらだらしてる〜？双葉杏の天気予報の時間だよー",
            "おはよー、朝の仕事は眠いよ、ふわぁ…"
        ]
        self.goode_box = [
            "えー今夜の天気予報、杏の番なの？？しょーがないな…",
            "みんな、お仕事お疲れ様〜。今夜の天気予報だよ。",
            "ふわぁ…もう夜だよ。眠くなってきちゃった。"
        ]
        self.special =[
            'え〜、新年も天気予報やるの？正月ぐらいゴロゴロさせてよ〜',
            'ふふふ、今日はバレンタイン、合法的におやつが食べられる日！',
            'んー、ひし餅もあられもおいしー…ひな祭りって楽しいかも♪',
            'デレステ配信{}周年おめでとう！お祝いのケーキはないのかっ？'.format(japan.year-2015),
            'ハロウィンはお祭りなんだよ！だから天気予報は中止！…だめぇ？',
            'モバマス配信{}周年おめでとう！杏もよく働いたなぁ…'.format(japan.year-2011),
            'メリークリスマス！今日の杏は上機嫌だぞ！'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度でーす。".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = [
            "{}は雨も風も強いし、仕事なんかしてる場合じゃない！杏を帰らせろー！".format(date),
            "{}は天気が悪いだって！？じゃあお仕事はおやすみ〜".format(date)
            ]
        self.d_text["rain_123"] = "{}は一日中降水確率が{}％を越えそうだから外に出ないほうがいいよ。".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "{}は午前中の降水確率が{}％、午後は{}％だって…傘を忘れずに持っていってね♪".format(date,self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％だから、朝に雨が降ってなくても、傘を持っていこう！".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％。夕方から雨が降りそうだから杏は早くかーえろっと。".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％だよ。傘を忘れずにね〜".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差の激しい１日になるよ。脱ぎ着のしやすい服を着よう！".format(date)
        self.d_text["under10"] = [
            "寒いな〜。杏はおうちに帰りたいよー。",
            'うーん、杏は北海道育ちだから慣れてるけど…結構冷えるねぇ。'
            ]
        self.d_text["under0"] = [
            "こんな寒い日は、こたつの中でゴロゴロするのが１番！",
            'ちょっと、杏は体が小さいから余計に寒いんだよ！そういう所、考えてよね〜'
            ]
        self.d_text["over30"] = [
            'はぁ、杏ちゃん脱水症状かも。早く帰ろ〜？',
            "あつーい、エアコンの効いた部屋から出られないよ。"
            ]
        self.d_text["over25"] = [
            '暑いなら、無理しないで休もう？',
            'みんな、水分補給してね？スタドリでもいいよ。'
            ]
        self.d_text['w_over30'] = [
            '今日も暑いよ〜。杏はトロピカルでエレガントな休日を要求するっ！',
            '暑さ対策が麦わら帽子とアイス１本じゃあ、もうダメ…ばたり…',
            '海の思い出？えーと…なんにもしなかった思い出！以上っ'
            ]
        self.d_text['w_under0'] = [
            'こんな寒いのに、みんな働いて偉いねぇ。無理はしすぎちゃダメだよ！',
            '今日も寒いね〜。可動式のこたつなんて、ないかな〜'
            ]
        self.d_text["fine"] = [
            "{}はとってもいい天気！お昼寝日和だぁ〜！".format(date),
            '{}はいい天気だ！たまには外でお昼寝するのもいいかも。'.format(date)
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で一番低いんだって。ちょっと寒そう".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番冷え込むみたいだよ。風邪をひかないようにね。".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はここ最近で一番暖かいみたい。快適に寝れそう…".format(date),
            1 :"{}はここ最近で一番の暑さだって。杏、暑いのはダメ…ばたり…".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いって。ちょっと薄着がいいんじゃない？".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}は{}よりも{}度も暖かいようですねぇ。ちょっと薄着にしたほうがいいね。".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}は{}よりも{}度も暑いみたい。急な暑さで倒れちゃうかも…".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}は{}よりも最低気温が{}度も高いって。ちょっと薄着がいいかも。".format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}は{}よりも最高気温が{}度も低いよ。出かけるなら、少し厚着をしてね〜'.format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}は{}よりも最低気温が{}度も低いって。急に寒くて慣れないよ〜'.format(date,pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = [
            "{}はさらに雪が積もりそうだよ。杏の実家はもっと積もるけどね".format(date),
            "ふぅ、まさか外で雪合戦につき合わされるなんて…みんな子供なんだからぁ",
            ]
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
        'term':'am_pm','cases':2,'border':1,
        1 : "{}はさらに雪が積もりそう。うーん、外に出たくない…".format(date),
        0 : '現在の積雪は{}cm。{}はもっと積もるかもだって。'.format(s_data[3][0],date)
        }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = "雪降るの？雪用の靴、どこに置いたっけ〜？"
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmだよ。ブーツと手袋で出かけよう。".format(s_data[3][0]),
            1 : 'おっきい方の雪だるまがきらりで、小さいほうが杏だよ！'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "解けかけの雪は滑るから注意だよー。"

        self.d_text['nothing_am']= [
            "それじゃあみんな、行ってらっしゃ〜い！えっ…杏も？",
            'じゃあ事務所に帰ってもうひと眠りするか…え、だめ！？',
            "{}もゆる〜く行こうよ…ね♪".format(date),
            '夜の天気予報もチェックよろしく〜'
            ]
        self.d_text['nothing_pm']=[
            'じゃあ、みんなおやすみ〜…ぐ〜…',
            'はい、天気予報頑張ったから、飴くれ！',
            "{}もゆる〜く行こうよ…ね♪".format(date),
            '明日の天気予報もチェックしてね〜',
            '次のお休みは明日だよね〜？'
            ]
        self.d_text['special'] = [
            '今年こそゴロゴロダラダラできる一年になりますよーに！',
            '杏がチョコをあげるなんて貴重だぞ！はい、あ〜ん',
            'ねぇ、杏はお雛様なんだからさ、もっと貢ぎ物をもらってもいいと思うんだよね。',
            'これからもデレステをプレイしてね〜',
            'トリックオアトリート！ほらほら、杏にお菓子を頂戴っ♪',
            'これからもモバマスをよろしく〜',
            '杏はいい子だったから、きっといっぱいプレゼントがもらえるはずっ！'
            ]
        self.d_text['kinrou'] = '今日は勤労感謝の日。杏の日頃の労働に免じて有休を要求する！'

        if cond[1] == 0:
            self.c_text = cf.special_day(japan,self.d_text['special'])
            if self.c_text == None:
                if japan.month == 11 and japan.day == 23: self.c_text = self.d_text['kinrou']
                elif am_pm == 0: self.c_text = cf.rand_sel(self.d_text['nothing_am'])
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
    cin = Anzu(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは双葉杏の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
