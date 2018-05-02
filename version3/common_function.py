# 文字数チェックに関わる関数
def show_text(show,text):
    if show =="1": print(text)

def mini_check(show,length,box):
    def omit(a,i,store):
        if i != store: y = str(len(a))+' '*3+i+' '*abs(12-len(i))+': '+a
        else: y = str(len(a))  + ' '*15+': '+a
        return y
    longest = 0
    text = ""
    store = ''
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
                    if type(j)==list:
                        for k in j:
                            i_num =0
                            i_txt = i+" [{}]".format(i_num)
                            show_text(show,omit(k,i_txt,store))
                            store = i_txt
                            i_num+=1
                            if len(k) >= longest:
                                longest = len(k)
                                text = k
                    else:
                        show_text(show,omit(j,i,store))
                        store = i
                        if len(j) >= longest:
                            longest = len(j)
                            text = j
            elif type(box[i])==dict:
                for key in box[i]:
                    if type(key)==int:
                        show_text(show,omit(box[i][key],i,store))
                        store = i
                        if len(box[i][key]) >= longest:
                            longest = len(box[i][key])
                            text = box[i][key]
            else:
                show_text(show,omit(box[i],i,store))
                store = i
                if len(box[i]) >= longest:
                    longest = len(box[i])
                    text = box[i]
    atn = ''
    if show =='1': atn = '*'*5+' '
    if longest > length:
        print("{}最長のものが{}文字で規定の長さ{}文字を超えています。".format(atn,longest,length))
        print("最長の文章は\n",text)
    else:
        print("{}最長のものが{}文字なので規定の長さ{}文字以内を満たしています。".format(atn,longest,length))
    print("-"*50)

def length_check(show,box_list,tx1=33,tx3=48):
    if tx1+tx3==81:
        print()
        print("<< goodm_boxの確認 >>")
        mini_check(show,tx1,box_list[0])
        print("<< goode_boxの確認 >>")
        mini_check(show,tx1,box_list[1])
        print("<< specialの確認 >>")
        mini_check(show,tx1,box_list[2])
        print("<< text2の確認 >>")
        print(len(box_list[3]+box_list[4]),"words　(45文字以下ならOK)")
        print("-"*50)
        print("<< d_textの確認 >>")
        mini_check(show,tx3,box_list[5])
    else: print("\n引数tx1とtx3の合計が81になるようにしてください\n")


#特別な日の判別に関わる関数
def special_day(japan,box):
    if japan.month==1 and japan.day<=3:       ans = box[0] if type(box[0])==str else rand_sel(box[0])
    elif japan.month==2 and japan.day==14:    ans = box[1] if type(box[1])==str else rand_sel(box[1])
    elif japan.month==3 and japan.day==3:     ans = box[2] if type(box[2])==str else rand_sel(box[2])
    elif japan.month==9 and 3<=japan.day<=5:  ans = box[3] if type(box[3])==str else rand_sel(box[3])
    elif japan.month==10 and japan.day==31:   ans = box[4] if type(box[4])==str else rand_sel(box[4])
    elif japan.month==11 and 27<japan.day<31: ans = box[5] if type(box[5])==str else rand_sel(box[5])
    elif japan.month==12 and 23<japan.day<26: ans = box[6] if type(box[6])==str else rand_sel(box[6])
    else: ans = None
    return ans

#文字数の省略
def rbs(x):
    y = round(abs(x))
    return y

import numpy.random as nmr
def rand_sel(a):
    return a[nmr.randint(len(a))]
