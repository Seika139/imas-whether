# 文字数チェックに関わる関数
def show_text(show,text):
    if show =="1": print(text)

def mini_check(show,length,box):
    longest = 0
    text = ""
    if type(box)==list:
        for i in box:
            show_text(show,str(len(i))+': '+i)
            if len(i) >= longest:
                longest = len(i)
                text = i
    elif type(box)==dict:
        for i in box:
            if type(box[i])==list:
                for j in box[i]:
                    show_text(show,str(len(j))+': '+j)
                    if len(j) >= longest:
                        longest = len(j)
                        text = j
            else:
                show_text(show,str(len(box[i]))+': '+box[i])
                if len(box[i]) >= longest:
                    longest = len(box[i])
                    text = box[i]
    if longest > length:
        print("最長のものが{}文字で規定の長さ{}文字を超えています。".format(longest,length))
        print("最長の文章は\n",text)
    else:
        print("最長のものが{}文字なので規定の長さ{}文字以内を満たしています。".format(longest,length))
    print("-"*50)

def length_check(show,box_list):
    print()
    print("<< goodm_boxの確認 >>")
    mini_check(show,33,box_list[0])
    print("<< goode_boxの確認 >>")
    mini_check(show,33,box_list[1])
    print("<< specialの確認 >>")
    mini_check(show,33,box_list[2])
    print("<< text2の確認 >>")
    print(len(box_list[3]+box_list[4]),"words　(45文字以下ならOK)")
    print("-"*50)
    print("<< d_textの確認 >>")
    mini_check(show,48,box_list[5])

def special_day(japan,box):
    if japan.month==1 and japan.day<=3:
        ans = box[0]
    elif japan.month==2 and japan.day==14:
        ans = box[1]
    elif japan.month==3 and japan.day==3:
        ans = box[2]
    elif japan.month==9 and 3<=japan.day<=5:
        ans = box[3]
    elif japan.month==10 and japan.day==31:
        ans = box[4]
    elif japan.month==11 and 28<=japan.day<=30:
        ans = box[5]
    elif japan.month==12 and 24<=japan.day<=25:
        ans = box[6]
    else:
        ans = None
    return ans
