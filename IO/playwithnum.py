import math
n,q=[int(x) for x in input().split()]
y=[0]+list(map(int,input().split()))
for i in range(n):
    y[i+1]+=y[i]
for i in range(q):
    l,r=map(int,input().split())
    m=math.floor((y[r]-y[l-1])/(r-l+1))
    print(m)
