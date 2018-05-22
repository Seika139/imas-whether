import numpy.random as nmr
import datetime as dt
import common_function as cf

class Yoshino:
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
            greet = "おはようございますー"
        else:
            date = "明日"
            pre_date = "今日"
            ht = "#デレマス夜の天気予報"
            greet = "こんばんはー"

        """ 1. 挨拶 """

        self.goodm_box = [
            "おはようございますー。わたくしの天気予報をお聞きくださいませー",
            "みなさまー、お目覚めですか？依田芳乃の天気予報の時間でしてー",
            'ずいぶんと遅い目覚めでしてー、今日のよき日は始まっていますよー'
            ]
        self.goode_box = [
            "こんばんはー。わたくし依田は芳乃が、{}の天気をお伝えするのでしてー".format(date),
            "お仕事お疲れ様ですー。今宵の依田芳乃の天気予報の時間でしてー",
            'みなさんこんばんはー。今回の天気予報を務める依田は芳乃と申しますー'
            ]
        self.special =[
            'あけましておめでとうございますー。新年も天気予報は休まないのでしてー',
            '{}。今日はばれんたいんでーなのでしてー'.format(greet),
            '{}。本日は桃の節句、ひな祭りなのでしてー'.format(greet),
            'デレステ{}周年の節目をー、みなと迎えられたことが何よりの喜びでしてー'.format(japan.year-2015),
            'ほぉー…みなが騒がしいのは、はろうぃんだからでしてー？',
            'モバマス{}周年、みなと歩んできた年月に感謝と祝福をー'.format(japan.year-2011),
            'めりーくりすますー、あいどるになってからは馴染みのある祭日でしてー'
            ]

        self.aisatsu = cf.special_day(japan,self.special)
        if self.aisatsu == None:
            if am_pm == 0: self.aisatsu = cf.rand_sel(self.goodm_box)
            else: self.aisatsu = cf.rand_sel(self.goode_box)

        """ 2. 予報 """

        self.tenki = "{}の{}の天気は「{}」、".format(date,self.place,self.weather)
        self.kion = "最高気温は{}度、最低気温は{}度となるでしょー".format(self.kion_max,self.kion_min)

        """ 3. 締め　"""

        self.d_text = {}
        self.d_text["storm"] = "{}は天気が優れないゆえー、なるべく外出はお控えくださいませー".format(date)
        self.d_text["fine"] = [
            "{}は良き天気になるようでしてー。日輪の恵みを、その手にー".format(date),
            '{}はお日柄も良くー探しもの日和となりましょうー'.format(date)
            ]
        self.d_text["rain_123"] = "{}は１日を通して降水確率が{}％を越えそうなので傘が必要でしてー".format(date,min(self.rain[1:]))
        self.d_text["rain_12"] = "午前中の降水確率が{}％、午後は{}％でしてー。傘を持っていくのがよいかとー".format(self.rain[1],self.rain[2])
        self.d_text["rain_23"] = "午後の降水確率が{}％、夜は{}％でしてー。雨が降ってなくても傘を持たれるのがよいかとー".format(self.rain[2],self.rain[3])
        self.d_text["rain_3"] = "{}は夜の降水確率が{}％でしてー。遅くまで外出する人は傘を持たれるのがよいかとー".format(date,self.rain[3])
        self.d_text["rain_2"] = "{}は午後の降水確率が{}％でしてー。出かける時は傘を持たれるのがよいかとー".format(date,self.rain[2])
        self.d_text["kionsa"] = '{}は気温差の激しい１日になりますゆえー。お体を壊さぬよう、気をつけくださいませー'.format(date)
        self.d_text["under10"] = [
            "{}は冷え込みますゆえー、暖かい格好で出かけなさいませー".format(date),
            "寒い日の温泉は温かさがより体に染み渡るのでしてー"
            ]
        self.d_text["under0"] = [
            "厚めのこーとを着ましょうー、寒さが厳しいゆえー",
            "指先が冷たくとも、心はほかほか温かいのでしてー"
            ]
        self.d_text['w_under0'] = {
            'term':'am_pm','cases':2,'border':1,
            1: '今日も寒い一日だったゆえー、湯に浸かって体を温めましょー',
            0: '本日もみなの白い吐息が寒さを感じさせるようでしてー'
            }
        self.d_text["over30"] = [
            "過ぎたるは猶及ばざるが如し…と言う様にー、冷房のつけすぎは、逆に体に良くないのでしてー",
            '心頭を滅却すれば火もまた涼し…と言うようにー、暑さに耐える力も時には必要でしてー'
            ]
        self.d_text["over25"] = [
            "疲れた時は休憩してはどうでしょー。少しの息抜きが心を鎮めますゆえー",
            "この暑き日ー、熱中症には気をつけくださいませー"
            ]
        self.d_text['w_over30'] = [
            "海で身を清めて、共にみそぎをいたしましょー",
            "暑い日が続きますゆえー、冷たいものを食べましょー",
            '海で食べるかき氷は､すばらしい体験でしてー。そなたにもこの感動をぜひー'
            ]
        self.d_text["w_cold_max"] = "{}は最高気温がここ一週間で最も低いゆえー、寒さにはお気をつけをー".format(date)
        self.d_text["w_cold_min"] = "{}はここ一週間で一番寒いゆえー、薄着はなりませぬー".format(date)
        self.d_text['w_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}はこの一週間で一番暖かいゆえー、普段よりも薄着が良いかとー".format(date),
            1 :"{}はこの一週間で一番の暑さゆえー、汗をかくような１日になるかとー".format(date)
            }
        self.d_text["w_hot_min"] = "{}はここ一週間で最低気温が一番高いゆえー、普段よりも薄着がよろしいかとー".format(date)
        self.d_text['y_hot_max'] = {
            'term':'kion_max','cases':2,'border':25,
            0 : "{}は{}より{}度も暖かくなるゆえー、気持ちのよい１日になるかとー".format(date,pre_date,cf.rbs(self.kion_max-s_data[0][0])),
            1 : "{}より{}度も暑くなるゆえー、急な暑さには気をつけなさいませー".format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
            }
        self.d_text["y_hot_min"] = "{}よりも最低気温が{}度高いのでしてー。{}よりも薄着がよろしいかとー".format(pre_date,cf.rbs(self.kion_min-s_data[1][0]),pre_date)
        self.d_text["y_cold_max"] = '{}よりも最高気温が{}度も低いゆえー、気温の変化に気をつけるのでしてー'.format(pre_date,cf.rbs(self.kion_max-s_data[0][0]))
        self.d_text["y_cold_min"] = '{}よりも最低気温が{}度も低いゆえー、暖かい格好が良いのでしてー'.format(pre_date,cf.rbs(self.kion_min-s_data[1][0]))
        #雪が降る＆積雪が十分にある
        self.d_text["snow_1-10"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : "たくさん雪が積もってましてー。空にはこれだけの雪があったのですねー",
            0 : '現在の積雪は{}cmですがー、さらに雪が積もるようでしてー'.format(s_data[3][0])
            }
        #雪が降る＆まあまあの積雪
        self.d_text["snow_1-1"] = {
            'term':'am_pm','cases':2,'border':1,
            1 : '街を彩る雪の花はー空からの贈り物なのでしてー',
            0 : '現在の積雪は{}cmですがー、今日も雪が積もるかもしれませぬー'.format(s_data[3][0])
            }
        #雪が降る＆積雪なし
        self.d_text["snow_1-0"] = '雪に足を取られぬようー、履物には気をつけなさいませー'
        #雪が降らん＆積雪が十分にある
        self.d_text["snow_0-10"] = {
            'term':'am_pm','cases':2,'border':1,
            0 : "現在の積雪は{}cmでしてー。雪道を歩く時はお気をつけてー".format(s_data[3][0]),
            1 : '積もった雪のせいで余計寒く感じるのでしてー'
            }
        #雪が降らん＆少しの積雪
        self.d_text["snow_0-1"] = "解けかけの雪は滑りますゆえー、何卒ご注意をー"

        self.d_text['nothing_am']= [
            "ぶおｰ､ぶおｰ｡法螺貝の音でみなを応援しますゆえー",
            "そなたに失せ物があれば、わたくしが探しますゆえー",
            "法螺貝には魔を払う力があるのでしてー。ぷおー、ぶおー",
            'すまほばかり見てはなりませぬー。前を見て歩くのでしてー'
            ]
        self.d_text['nothing_pm']=[
            "困っている人には力を貸しなさい…ばばさまのお言葉でしてー",
            "おやすみなさいませー。今宵もみなが安らかに眠れるようー",
            "法螺貝には魔を払う力があるのでしてー。ぷおー、ぶおー"
            ]
        self.d_text['special'] = [
            '手を合わせて祈りましょうー。今年も善き一年となりますようー',
            'みながちょこれーとを渡すのならばー、わたくしからは和菓子を差し上げるのでしてー',
            'ばばさまに頂いた雛壇がとても豪華絢爛なのでしてー',
            'みなの声を背に、次なる舞台へ歩み続けましょー。みなの行く先に幸多からんことをー',
            'お菓子をよこせですかー？煎餅しか持ってないのですがそれでもよろしくてー？',
            '万感の思いで迎える記念日でしてー、支えてくださるみなみなに感謝をー',
            'この一年を支えていただいたことに、大いなる感謝をー。次の一年も、期待いたしませー'
            ]
        self.d_text['hanami'] = [
            "みなの住まう所では、桜は咲いてますでしょうかー？こちらの桜は綺麗でしてー",
            "先日は紗枝さんとお花見にいったのでしてー",
            '桜の花吹雪ー、舞い散る桜とともに踊りましょー'
            ]
        self.d_text['momiji'] = [
            '紅葉は美しく散りー、そしてまた次の季節を迎えー…巡るものー…',
            'もみじ葉の移りゆく色はーまるであいどるのようでしてー',
            'みなの住まうところではー木の葉は色づいているでしょうかー？'
            ]

        if cond[1] == 0:
            self.c_text = cf.special_day(japan,self.d_text['special'])
            if self.c_text == None:
                if japan.month==4 and japan.day<=10: self.c_text = cf.rand_sel(self.d_text['hanami'])
                elif japan.month==3 and japan.day>=25: self.c_text = cf.rand_sel(self.d_text['hanami'])
                elif japan.month==11 and japan.day>=18: self.c_text = cf.rand_sel(self.d_text['momiji'])
                elif am_pm == 0: self.c_text = cf.rand_sel(self.d_text['nothing_am'])
                else: self.c_text = cf.rand_sel(self.d_text['nothing_pm'])
        elif cond[1]<=10 and japan.month== 4 and japan.day<=10: self.c_text = cf.rand_sel(self.d_text['hanami'])
        elif cond[1]<=10 and japan.month== 3 and japan.day>=25: self.c_text = cf.rand_sel(self.d_text['hanami'])
        elif cond[1]<=10 and japan.month==11 and japan.day>=18: self.c_text = cf.rand_sel(self.d_text['momiji'])
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
    cin = Yoshino(am_pm,japan,gt.gt_box_array[am_pm],setter.cond_key,setter.s_data)
    print("このモジュールは依田芳乃の天気予報をお伝えします。")
    print("文字数のチェックを実施します。")
    n = input("全てのテキストを見る場合は「1」と打ち込んでください\n>> ")
    box_list = [cin.goodm_box,cin.goode_box,cin.special,cin.tenki,cin.kion,cin.d_text]
    cf.length_check(n,box_list,35,46)
    n2= input("ツイートと同じ文章を見るなら「2」と打ち込んでください\n>> ")
    if n2 =="2":
        print(cin.f_text)
