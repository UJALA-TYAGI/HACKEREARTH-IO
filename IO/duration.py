import math
t=int(input())
while t>0:
    sh,sm,eh,em=[int(x) for x in input().split()]
    st=sm+60*sh
    et=em+60*eh
    dur=et-st
    dh=math.floor(dur/60)
    dm=dur%60
    print(dh,dm)
    t=t-1
