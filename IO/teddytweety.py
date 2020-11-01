n=int(input())
a=int(n/3)
n=n-a
b=int(n/2)
n=n-a
c=n

if (a==b) and (b==c):
    print('YES')
else:
    print('NO')
