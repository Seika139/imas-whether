text1 = "ふふーん！ボクの天気予報を見れるなんてあなたは幸せ者ですねぇー"
text2 = "明日の東京の天気は「晴れのち時々くもり」、最高気温は20度、最低気温は16度の予報です。"
text3 = '暑くて眠れない夜はボクを数えてください！ほら、カワイイ幸子が１人、カワイイ幸子が２人...'
text4 = "#デレマス朝の天気予報"
text = ""
for i in [text1,text2,text3,text4]:
    text += i +"\n"
    print(i)
    print(len(i), "words")
    print()
print(text)
print(len(text)-1, "words")

a = {"QWER":13,"QWERT":1234}
for i in a:
    print(i,a[i])
