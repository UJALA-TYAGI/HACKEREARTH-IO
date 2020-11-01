import math
n=int(input())
motu=[]
patlu=[]
for i in range(1,math.floor(n/3)):
    patlu.append(i)
    motu.append(2*i)
    s=int(sum(patlu)+sum(motu))
    if s>n:
        break
a=patlu[len(patlu)-1]
motu.remove(motu[len(motu)-1])
sum=int(int(sum(patlu))+int(sum(motu)))
motu.append(n-sum)
b=motu[len(motu)-1]
if (a>b or sum<n) and (b>0):
    print('Motu')
if (sum>n) and (b<0):
    print('Patlu')
