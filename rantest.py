import numpy.random as nmr
num = nmr.randint(0,7,4)
print(num)
while num[0] == num[1]:
    num[1] = nmr.randint(7)
while num[2] in num[:2]:
    num[2] =  nmr.randint(7)
while num[3] in num[:3]:
    num[3] =  nmr.randint(7)
print(num)
print(num[:2])
