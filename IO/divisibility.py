n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    l.append(i%10)
num=int(''.join(str(i) for i in l))
if num%10==0:
    print('Yes')
else:
    print('No')

#function to find last digit of a number
#lastdigit = (repr(x)[-1])
