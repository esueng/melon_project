
#csv 파일 읽기

import csv
import pandas as pd
l = []
 
f = open("C:/Users/PC/Desktop/BDPFINAL00.csv","rt")
reader = csv.reader(f)
 
for row in reader:
    l.append(row[2])

l2 = []
l3 = []
l4 = []
c0 = 0

#중복되지 않은 list

for v in l:
    if v not in l2:
        l2.append(v)

#최대 유지 기간

for r in l2:
    d0 = 0
    for e in l:
        if e == r:
            c0 = c0+1
            if c0 >= d0:
                d0 = c0
            else:
                continue
        else:
            c0 = 0
    l3.append(d0)

# 처음 차트 진입부터 최근 차트


for i in l2:
     a = 0
     b = 0
     for x in l:
         c = l.index(i)
         if i == x:
             b = 0
         else:
             b = b+1
             if b >= a:
                 a = b
             else:
                 continue
         d = len(l) - 1 - c
     if b > d:
         g = b-d+1
     elif b < d:
         g = d-b+1
     else:
         g = 1
     l4.append(g)
l11=[l2,l3,l4]
l11=list(map(list,zip(*l11)))
dataframe=pd.DataFrame(l11)
dataframe.to_csv("C:/Users/PC/Desktop/BDPFINALanalysis.csv",header=False,index=False,encoding='utf-8-sig')

print(l2,l3,l4)


