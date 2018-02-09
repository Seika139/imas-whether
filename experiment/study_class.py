#encoding:utf-8
class Study:
    def __init__(self):

        def aisatu(self):
            print("おはようございます")
            self.kon = "こんばんは"
            return self.kon

        self.ai2 = aisatu(self)+"、いい天気ですね"
        print(self.kon)

    def c0(self):
        if int(input("0")) == 0: print("0000")

std = Study()
print(std.ai2)
std.c0()

a = "ここ"
if "１" or "こ" in a:
    print("www")
