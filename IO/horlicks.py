d=int(input())
r=[]
h=[]
t=0
for i in range(d):
    a,b=[int(x) for x in input().split()]
    r.append(a)
    h.append(b)
for (a,b) in zip(r,h):
    ar=int(2*(22/7)*a)
    cap=100*b
    if cap>=ar:
        t+=1
print(t)
