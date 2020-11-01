import math
t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    if ((b-a)-(c-b)) == 0:
        print(b-a,c-b)
        print(0)
    else:
        print(math.ceil(abs((b-a)-(c-b))/2))
        print((((b-a)-(c-b))/2))
