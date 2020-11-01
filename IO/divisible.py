import math
n=int(input())
y=[*range(0,n)]
y=[int(x) for x in input().split()]
l=len(y)
a=[]
b=[]
for i in range(math.ceil(l/2),l):
    b.append(y[i])
for i in range(0,math.floor(l/2)):
    a.append(y[i])
m=[]
n=[]
for (k,l) in zip(a,b):
    k=[int(x) for x in str(k)]
    m.append(k[0])
    l=[int(x) for x in str(l)]
    n.append(l[len(l)-1])
a=m+n
num=int(''.join(str(i) for i in a))
if num%11==0:
    print('OUI')
else:
    print('NON')
