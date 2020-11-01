n=int(input())
a=[]
y=[*range(n)]
y=[int(x) for x in input().split()]
a.append(y)
print(a)
ans=1
for items in a:
    for item in items:
        print(item)
        an=int(item)
        ans=(ans*item)
print(ans%1000000007)
