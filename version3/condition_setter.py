import numpy.random as nmr
import datetime as dt

class Setter:
    """
    キャラごとに条件の判断を行うとメンテナンスが大変なので、condition_setterで一括管理を行う。
    キャラごとに設定したい条件についてはキャラごとに行う。
    """

    def __init__(self,am_pm,data,prediction):
        self.place = prediction[0]
        self.day = prediction[1]
        self.weather = prediction[2]
        self.weather_id = prediction[3]
        self.kion_max = prediction[4][0]
        self.kion_min = prediction[4][1]
        self.rain = prediction[6]
        """
    def __init__(self,box,time,record):
        self.place = box[0]                 #　"東京"
        self.reporting_date = box[1]        # 2018/03/15
        self.weather = box[2]               # 晴れ時々くもり
        self.weather_id = box[3]            # http://www.drk7.jp/MT/images/MTWeather/101.gif
        self.kion_box = box[4]              # ['22', '8']
        self.jikantai = box[5]              # ['00-06', '06-12', '12-18', '18-24']
        self.rain = box[6]                  # 降水確率 [10,10,10,10] の形
        self.time = time                    # 0か1　0なら朝の天気予報、1なら夜の天気予報
        """
        kion_max_array = []
        kion_min_array =[]
        snow_fall_array = []
        snow_depth_array = []
        tenki_gaikyou_array = []
        sunshine_hour_array = []
        for i in range(len(data)):
            kion_max_array.append(data[i]["気温"]["最高"])
            kion_min_array.append(data[i]["気温"]["最低"])
            snow_fall_array.append(data[i]["雪"]["降雪"])

            try:
                snow_depth_array.appned(data[i]["雪"]["最深積雪"])
            except Exception as e:
                snow_depth_array.append(0)

            tenki_gaikyou_array.append(data[i]["天気概況"]["昼"])
            sunshine_hour_array.append(data[i]["日照時間"])

        self.s_data = [
            kion_max_array,
            kion_min_array,
            snow_fall_array,
            snow_depth_array,
            tenki_gaikyou_array,
            sunshine_hour_array
        ]

        self.cond_dic = {
        "snow_1-10" : 0, #雪が降る＆積雪が十分にある
        "snow_1-1" : 0, #雪が降る＆まあまあの積雪
        "snow_1-0" : 0, #雪が降る＆積雪なし
        "snow_0-10" : 0, #雪が降らん＆積雪が十分にある
        "snow_0-1" : 0, #雪が降らん＆少しの積雪
        "storm": 0,
        "rain_123": 0,
        "rain_12": 0,
        "rain_23": 0,
        "rain_3": 0,
        "rain_2": 0,
        "kionsa" : 0,
        "under10" : 0,
        "under0" : 0,
        "over30" : 0,
        "over25" : 0,
        "fine" : 0,
        "w_cold_max" : 0,#今週で一番最高気温が低い
        "w_cold_min" : 0,#今週で一番最低気温が低い
        "w_hot_max" : 0,#今週で一番最高気温が高い
        "w_hot_min" : 0,#今週で一番最低気温が高い
        "y_hot_max" : 0,#昨日より最高気温がとても高い
        "y_hot_min" : 0,#昨日より最低気温がとても高い
        "y_cold_max" : 0,#昨日より最高気温がとても低い
        "y_cold_min" : 0,#昨日より最低気温がとても低い
        'w_over30' : 0,#30度以上の日が続く
        'w_under0' : 0 #0度以下の日が続く
        }

        ## 予報のみで判断できるもの

        #嵐
        if "307" in self.weather_id or "308" in self.weather_id:
            self.cond_dic["storm"] = 100
        #雨
        if "雨" in self.weather or min(self.rain) >= 10:
            if min(self.rain[1],self.rain[2],self.rain[3]) >= 30:
                self.cond_dic["rain_123"]  = 80     #1日を通して降水確率が30%以上
            elif min(self.rain[1],self.rain[2]) >= 30:
                self.cond_dic["rain_12"] = 70      #午前と午後の降水確率が30%以上
            elif min(self.rain[2],self.rain[3]) >= 30:
                self.cond_dic["rain_23"] = 70    #午後と夜の降水確率が30%以上
            elif self.rain[3] >= 30:
                self.cond_dic["rain_3"] = 60     #夜の降水確率が30%以上
            elif self.rain[2] >= 30:
                self.cond_dic["rain_2"] = 60      #午後の降水確率が30%以上

        #最低気温が0度以下
        if int(self.kion_min) <= 0:
            self.cond_dic["under0"] = 30
        #最高気温が10度以下
        if int(self.kion_max) <= 10:
            self.cond_dic["under10"] = 20
        #気温が30度以上
        if int(self.kion_max) >= 30:
            self.cond_dic["over30"] = 35
        #熱帯夜　最低気温が25度以上
        if int(self.kion_min) >= 25:
            self.cond_dic["over25"] = 30

        #ただの「晴れ」の場合
        if "100" in self.weather_id:
            self.cond_dic["fine"] = 10

        # 気温差
        kionsa = float(self.kion_max) - float(self.kion_min)
        if kionsa >= 20:
            self.cond_dic["kionsa"] = 60
        elif kionsa >= 15:
            self.cond_dic["kionsa"] = 40
        elif kionsa >= 12:
            self.cond_dic["kionsa"] = 20

        ## データが必要だが夜の天気でも大丈夫
        """
        dataの中身が全部入ってないとエラーになる
        これにはsetterにdateを与える時に工夫が必要で、
        詳しくは　twwet_v3.py の
        if am_pm == 1:
        の文にある
        """
        max_dis_w = float(self.kion_max) - max(kion_max_array)
        max_dis_d = float(self.kion_max) - kion_max_array[0]
        min_dis_w = float(self.kion_min) - min(kion_min_array)
        min_dis_d = float(self.kion_min) - kion_min_array[0]

        if max_dis_w >= 16:
            self.cond_dic["w_hot_max"] = 80
        elif max_dis_w >= 12:
            self.cond_dic["w_hot_max"] = 60
        elif max_dis_w >= 8:
            self.cond_dic["w_hot_max"] = 40
        elif max_dis_w <= -16:
            self.cond_dic["w_cold_max"] = 80
        elif max_dis_w <= -12:
            self.cond_dic["w_cold_max"] = 60
        elif max_dis_w <= -8:
            self.cond_dic["w_cold_max"] = 40

        if min_dis_w >= 16:
            self.cond_dic["w_hot_min"] = 80
        elif min_dis_w >= 12:
            self.cond_dic["w_hot_min"] = 60
        elif min_dis_w >= 8:
            self.cond_dic["w_hot_min"] = 40
        elif min_dis_w <= -16:
            self.cond_dic["w_cold_min"] = 80
        elif min_dis_w <= -12:
            self.cond_dic["w_cold_min"] = 60
        elif min_dis_w <= -8:
            self.cond_dic["w_cold_min"] = 40

        if max_dis_d >= 16:
            self.cond_dic["y_hot_max"] = 80
        elif max_dis_d >= 12:
            self.cond_dic["y_hot_max"] = 60
        elif max_dis_d >= 8:
            self.cond_dic["y_hot_max"] = 40
        elif max_dis_d <= -16:
            self.cond_dic["y_cold_max"] = 80
        elif max_dis_d <= -12:
            self.cond_dic["y_cold_max"] = 60
        elif max_dis_d <= -8:
            self.cond_dic["y_cold_max"] = 40

        if min_dis_d >= 16:
            self.cond_dic["y_hot_min"] = 80
        elif min_dis_d >= 12:
            self.cond_dic["y_hot_min"] = 60
        elif min_dis_d >= 8:
            self.cond_dic["y_hot_min"] = 40
        elif min_dis_d <= -16:
            self.cond_dic["y_cold_min"] = 80
        elif min_dis_d <= -12:
            self.cond_dic["y_cold_min"] = 60
        elif min_dis_d <= -8:
            self.cond_dic["y_cold_min"] = 40

        if min(float(self.kion_max),min(kion_max_array[:3])) >= 30:
            self.cond_dic['w_over30'] = 50
        if max(float(self.kion_min),max(kion_min_array[:3])) <= 0:
            self.cond_dic['w_under0'] = 50

        ## データが必要で朝の天気でしか使えない
        """
        << 雪 >>
        < 昼 >
        積雪..　10以上 1以上　なし
        降雪..　あり　なし
        < 夜 >
        昼間の天気予報.. 雪　雪なし
        積雪..　10以上 1以上　なし
        降雪..　あり　なし
        """
        #　積雪　昼用
        if am_pm == 0:
            if "雪" in self.weather and "雨か雪" not in self.weather:
                if type(snow_depth_array[0]) == float:
                    if snow_depth_array[0] >= 10:
                        self.cond_dic["snow_1-10"] = 80
                    elif snow_depth_array[0] >= 1:
                        self.cond_dic["snow_1-1"] = 60
                    else:
                        self.cond_dic["snow_1-0"] = 40
            elif type(snow_depth_array[0]) == float:
                if snow_depth_array[0] >= 10:
                    self.cond_dic["snow_0-10"] = 80
                elif snow_depth_array[0] >= 1:
                    self.cond_dic["snow_0-1"] = 60
        #　積雪　夜用
        elif am_pm == 1:
            snow_tupple = [0,0,0]
            if "雪" in self.weather and "雨か雪" not in self.weather:
                snow_tupple[0] = 1
            if type(snow_depth_array[1]) == float:
                snow_tupple[1] = snow_depth_array[1]
            else:
                snow_tupple[1] = 0
            yesterday_weather = data[0]["天気概況"]["昼"]
            yesterday_min = data[0]["気温"]["最低"]
            if "雪" in yesterday_weather and "雨か雪" not in yesterday_weather:
                snow_tupple[2] = 1

            if snow_tupple[0] == 1:
                if snow_tupple[1] >= 10:
                    self.cond_dic["snow_1-10"] = 80
                elif snow_tupple[1] >= 1 and snow_tupple[2]==1:
                    self.cond_dic["snow_1-1"] = 60
                else:
                    self.cond_dic["snow_1-0"] = 40
            else:
                if snow_depth_array[0] >= 10:
                    self.cond_dic["snow_0-10"] = 80
                elif snow_depth_array[0] >= 1 and snow_tupple[2]==1:
                    self.cond_dic["snow_0-1"] = 60

        #ここまで全部cond_dicに追加してきたが、この中で値が最大のものからランダムに一つ選ぶ
        cond_max = max(self.cond_dic.items(),key=lambda x:x[1])[1] #type=int
        cond_select = []
        for i in self.cond_dic:
            if self.cond_dic[i] == cond_max:
                cond_select.append(i)
        num = nmr.randint(len(cond_select))
        self.cond_key = [cond_select[num],cond_max] #[str,int]

    def open_info(self,data):
        def printer(day,weather,max,min):
            print("日付　　",day)
            print("天気　　",weather)
            print("最高気温",max)
            print("最低気温",min)
            print("="*50)

        print("場所　　",self.place)
        print()
        printer(self.day,self.weather,self.kion_max,self.kion_min)
        for i in data:
            printer(i["day"],i["天気概況"]["昼"],i["気温"]["最高"],i["気温"]["最低"])

if __name__ == "__main__":
    import recorder as rc
    import gt_v3

    now = dt.datetime.now()
    japan = now + dt.timedelta(hours=0)
    j_hour = japan.hour
    if 0 <= j_hour <= 12: am_pm = 0
    else: am_pm = 1

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

    setter = Setter(am_pm,data_base,gt.gt_box_array[am_pm])


    for i in data_base:
        print(i)
        print("-"*50)
    print("#"*55)
    for i in setter.cond_dic:
        print(i,setter.cond_dic[i])
    print("#"*55)
    print(gt.gt_box_array[am_pm])

    nm= input("input 1\n>> ")
    if nm=="1":
        setter.open_info(data_base)
