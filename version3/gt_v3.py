#encoding:utf-8

#モジュールのインポート
import xml.etree.ElementTree as ET
import urllib.request as ur

class Get_tenki:
    def __init__(self,url,p_id,place):
        self.url = url
        self.p_id = p_id
        self.place = place
        #urlを入れる
        self.req = ur.Request(self.url)

        #データの取得
        with ur.urlopen(self.req) as response:
            self.XmlData = response.read()
        self.root = ET.fromstring(self.XmlData)


        #それぞれの値の用意
        self.area = self.root.findall(".//area[@id='{}']".format(p_id))
        for youso in self.area:
            self.days = youso.findall("info")

            self.reporting_date_array = []
            self.weather_array = []
            self.weather_id_array = []
            self.kion_list_array = []
            self.kousuikakuritsu_array = []
            for day in self.days:
                self.reporting_date_array.append(day.get("date")) #予報する日付
                self.weather_array.append(day[0].text) #天気
                self.weather_id_array.append(day[1].text) #天気のid

                self.kion_list_array.append(day.findall(".//range"))
                self.kion_box = []
                for kion in self.kion_list_array:
                    self.x =[]
                    for j in range(len(kion)):
                        self.x.append(kion[j].text)
                    self.kion_box.append(self.x)

                self.jikantai = []
                self.rain = []
                self.kousuikakuritsu_array.append(day.findall(".//period"))
                for i in self.kousuikakuritsu_array:
                    self.y = []
                    self.z = []
                    for j in range(len(i)):
                        self.y.append(i[j].get("hour"))
                        self.z.append(int(i[j].text))
                    self.jikantai.append(self.y)
                    self.rain.append(self.z)

            self.gt_box_array = []
            for i in range(len(self.reporting_date_array)):
                array_set = [
                    self.place,
                    self.reporting_date_array[i],
                    self.weather_array[i],
                    self.weather_id_array[i],
                    self.kion_box[i],
                    self.jikantai[i],
                    self.rain[i]
                    ]
                self.gt_box_array.append(array_set)

if __name__ == "__main__":
    print("#"*100)
    koko = Get_tenki("http://www.drk7.jp/weather/xml/13.xml",'東京地方',"東京")
    print("このモジュールで{}の天気情報を取得しています。".format(koko.gt_box_array[0][0]))
    for i in range(7):
        print("日付　　　",koko.gt_box_array[i][1])
        print("天気　　　",koko.gt_box_array[i][2])
        print("gif　　　",koko.gt_box_array[i][3])
        print("気温　　　",koko.gt_box_array[i][4])
        print("時間帯　　　",koko.gt_box_array[i][5])
        print("降水確率　　　",koko.gt_box_array[i][6])
        print("*"*50)
