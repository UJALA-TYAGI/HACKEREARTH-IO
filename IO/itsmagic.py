n = int(input())
lst = list(map(int,input().split()))
ls = sorted(lst)
k=-1
s = sum(lst)
for i in range(n):
    res = s-ls[i]
    if res%7==0:
        k = ls[i]
        break
if k!=-1:
    print(lst.index(k))
else:
    print(k)
