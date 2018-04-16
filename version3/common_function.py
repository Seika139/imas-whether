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
