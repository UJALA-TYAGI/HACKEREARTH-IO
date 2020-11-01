import numpy as np
t=int(input())
total=[]
cost=[*range(0,2)]
while t>0:
    cost[0],cost[1]=[int(x) for x in input().split()]


    n=int(input())
    a=[]


    y=[*range(0,2)]
    for row in range (0,n,1):



        y=[int(x) for x in input().split()]



        a.append(y)



    totals=0
    arr=np.array(a)
    totals=np.sum(arr,axis=0)


    totals=sorted(totals)

    cost=sorted(cost)



    total.append(totals[0]*cost[1]+totals[1]*cost[0])

    t=t-1
print(*total,sep="\n")
