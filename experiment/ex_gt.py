#encoding:utf-8
def get_tenki(url,p_id,place):
    #モジュールのインポート
    import xml.etree.ElementTree as ET
    import urllib.request as ur

    #urlを入れる
    req = ur.Request(url=url)

    #データの取得
    with ur.urlopen(req) as response:
        XmlData = response.read()
    root = ET.fromstring(XmlData)


    #それぞれの値の用意
    area = root.findall(".//area[@id='{}']".format(p_id=p_id))
    for youso in area:
        place = youso.find('id')
        day1 = youso.find("info")
        reporting_date = day1.get("date")
        weather = day1[0].text
        weather_id = day1[1].text
        kion_list = day1.findall(".//range")
        kousuikakuritsu = day1.findall(".//period")
        kion_box = []
        for kion in kion_list:
            kion_box.append(kion.text)
        jikantai = []
        rain = []
        for i in kousuikakuritsu:
            jikantai.append(i.get("hour"))
            rain.append(int(i.text))

if __name__ == "__main__":
    print("このモジュールで{}の天気情報を取得しています。".format(place))
