import glob
import os
pictures = glob.glob('./pict/*')
for i in range(len(pictures)):
    os.rename(pictures[i],'./pict/yuko{}.jpg'.format(i+1))
pictures = glob.glob('./pict/*')
print(pictures)
