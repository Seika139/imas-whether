import numpy.random as nmr
import datetime as dt
import common_function as cf

class Rika:
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
            'やっほー☆城ヶ崎莉嘉だよー。アタシの天気予報、見て見て！',
            'みんな,おはー☆天気予報を見て、今日も一日ファイトだー！',
            'なんと、今日のリポーターはカリスマJCの莉嘉ちゃんでーす☆えへっ☆'
            ]
        self.goode_box = [
            "やっほー☆城ヶ崎莉嘉だよー。アタシの天気予報、見て見て！",
            'こんばんはー☆JC天気予報士のリカが明日の天気を教えちゃうよ！',
            'みんな〜お仕事お疲れ様ー☆アタシの天気予報見て元気だしてよねっ！'
            ]
        self.special =[
            'ハッピーニューイヤー！最高の新年にしようねっ☆',
            'ハッピーバレンタイン～♪アタシから、甘いLOVEのプレゼント〜☆',
            [cf.rand_sel(self.goodm_box),cf.rand_sel(self.goode_box)][am_pm],
            'デレステ{}周年おめでとー！パーティー楽しみだねっ♪'.format(japan.year-2015),
            'ハッピーハロウィン！仮装パーティー、何の仮装しよっかなー☆',
            'モバマス配信{}周年！つまりー、誕生日ってことだね♪おめでとう！'.format(japan.year-2011),
            'メリークリスマース！みんなにはこのリカちゃんをプレゼントだよっ☆'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None: self.aisatsu = cf.rand_sel(self.goode_box) if am_pm else cf.rand_sel(self.goodm_box)

        """ 2. 予報 """
        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度の予報でーす{}".format(self.kion_max,self.kion_min,cf.rand_sel(['!','♪','☆']))

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = "{}の天気最悪ー、お出かけできないじゃーん。ぶーぶー".format(date)
        self.d_text["fine"] = [
            "{}はいい天気だから…虫取りしにいこーよ！…え、だめぇ？".format(date),
            '{}はいい天気だから、気合い入れておしゃれしなきゃ！'
            ]
        self.d_text["rain_123"] = "{}は１日中降水確率が{}％を越えるんだって！傘を忘れずに持って行ってね☆".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "午前中の降水確率が{}％で、午後は{}％だよ！傘、どれ持ってこうかな〜".format(self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％だよ！雨が降ってなくても傘を持っていってね！".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％だよ！夜まで外出する人は傘をがあるといいみたい！".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％だって、傘がないと濡れちゃうゾ☆".format(date,self.rain[2])
        self.d_text["kionsa"] = "{}は気温差の激しいんだって！どの服を着たらいいのかな〜？".format(date)
        self.d_text["under10"] = [
            'ちょっと寒いけど、ガマンする！ 大丈夫☆',
            'くしゅん！ ちょっと寒いかも。みんなも風邪ひかないでね！'
            ]
        self.d_text["under0"] = [
            '寒いの？じゃ、アタシがあっためたげる☆',
            'ギャルだってお腹冷やすの、よくないもん！'
            ]
        self.d_text['w_under0'] = [
            "うー、寒いけど…ギャルは寒さになんか負けないんだからっ☆",
            'アタシ、冬好き☆みんなのあったかさ、いつもより超感じるから！'
            ]
        self.d_text["over30"] = [
            "ひまわり畑の中から～、ばぁー！！ 莉嘉だよー☆ほらっ、ひまわりの花、ちょーすごい！",
            'あれー、やらしー視線感じるー☆お姉ちゃんのマネ♪似てた？',
            '南国ビーチ、お待ちかねのセクシー水着！これはもう、ファンのみんなも大コーフン確定だよねっ！'
            ]
        self.d_text["over25"] = [
            "この前虫取りしてきたんだけど、何が取れたか見たい？見たい？",
            '水着でも、ワンポイントのオシャレが大事！アタシのこだわり、見て見て☆'
            ]
        self.d_text['w_over30'] = [
            'ひまわりの花びら、真っ黄っ黄だね！ ライオンのたてがみみたいっ。がおっ♪',
            'この夏一番のセクシーギャルだよ♪みんな、アタシの魅力で真っ赤になっちゃえー☆',
            'えへへ～☆青い海、白い砂浜……ってきたら、あとはビーチボール遊びだよね♪楽しみにしてたんだー☆'
            ]
        self.d_text["w_cold_max"] = "{}はここ一週間で最高気温が一番低いんだって！寒くてヤバいかも〜".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番寒いのかぁ…ヘソ出しは風邪引いちゃうかなぁ？".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はこの一週間で一番暖かいよ！この前買ったあの服を着ちゃおっと☆".format(date),
            1 :"{}はこの一週間で一番の暑さだって。これは海に行くしかねいよね☆".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いって！過ごしやすい１日になるかもー♪".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}より{}度も暖かくなるからー、ちょっと露出多めでいっちゃおう☆".format(pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}より{}度も暑いからー、熱中症には気をつけてね☆".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}よりも最低気温が{}度も高くなるよ！この前買ったあの服を着ちゃおっと☆".format(pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        self.d_text["y_cold_max"] = '{}よりも最高気温が{}度も低いからー、暖かくして出かけてね！'.format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}よりも最低気温が{}度も低いからー、暖かくして出かけてね！'.format(pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : 'じゃーん！今日のアタシは雪の妖精！雪の結晶って、宝石みたいでキラキラしててすっごいキレイだし！',
            0 : '今の積雪は{}cmだよ！もっと積もれー、かまくらが作れるくらい！'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : '雪だるま、みりあちゃんと小梅ちゃんは顔をつくってね？かわいくガッツリ盛ってあげて！',
            0 : '今の積雪は{}cmだよ！はやく雪だるま作りたいーー！'.format(s_data[3][0])
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = [
        '雪とかー、クリスタルとかー、キラキラ盛り盛りじゃない？アガるよねっ☆',
        '休み時間にみんなで雪合戦、できるかなー？'
        ]
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "今の積雪は{}cmだよ！ほら、みんなで作った雪だるま見て見て！".format(s_data[3][0]),
            1 : 'スケート初めてとは思えなくない？ほらほら、このスピード…わわっ！'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = [
            'スケート初めてにしてはアタシ結構イケてるよね？スイスイ滑れてるでしょー☆えへへー♪',
            '氷の上って滑りやすいよねー。気をつけて歩かないと転んじゃうよ！'
            ]

        self.d_text['nothing_am']= [
            "へへっ♪今度のオフはお姉ちゃんとイッパイ遊ぶぞ～♪てことで、変装はカンペキだよねっ☆",
            "フトンの中にいるそこの君、もう出かける時間だぞっ☆起きろーー！",
            "見て見てーっ☆アタシ、シールでもちょーカワイくない？やっぱカリスマアイドルのオーラだよねっ！",
            '今日もお仕事頑張るぞー！カリスマJCの本気見せちゃうんだからっ！'
            ]
        self.d_text['nothing_pm']=[
            "ゲーセンに来たからにはーやっぱこれでしょ！フルコンボできるまで、今日は帰れないんだからーっ☆",
            "お姉ちゃんにメイク手伝ってもらったのっ！キラキラしてるでしょ☆",
            'お仕事終わったらー、ゲーセン行きたいっ！でも門限すぎたら怒られちゃうし〜…',
            '今日はお姉ちゃんとお風呂入っちゃおっ！怒られないかなぁ…？ふふっ☆'
            ]
        self.d_text['special'] = [
            ['お姉ちゃんの手作りデコスペおせちー♪お先にいっただきまーす♪',
            'みんなの楽しいお正月♪アタシがいっぱい、めでたくしてあげる☆',
            'みんなに初リカのお披露目だよ♪今年もこの調子でヨロシクなんだから！'],
            ['チョコ…食べすぎ！ って、いつもお姉ちゃんに怒られちゃうんだ…',
            '今夜のリカは、ちょっとオトナなの☆へへっ♪'],
            [cf.rand_sel(self.d_text['nothing_am']),cf.rand_sel(self.d_text['nothing_pm'])][am_pm],
            '今日の記念パーティーはレディの着こなし！最後まで、上品に……',
            'みんなとお菓子の交換するんだ！あ、杏ちゃんもう食べてるっ！',
            ['アニバーサリーのライブだよ！唯ちゃんと加蓮ちゃんとカメラにピース☆',
            '今まで以上に頑張ってトップ目指さないとダメだよね♪ よ～し、JCの本気を見せちゃうぞ！'],
            ['アタシがサンタになったらプレゼントの大争奪戦が起きちゃうよねっ☆よーっし、配っちゃうぞーっ！',
            'ブリッチャ…ブリッツ…ン？ んぁー！ わかんないけど借りてきたよっ！']
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
    cin = Rika(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは城ヶ崎莉嘉の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
