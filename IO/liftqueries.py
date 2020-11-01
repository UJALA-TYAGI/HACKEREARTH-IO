t=int(input())
high=7
low=0
while t>0:
    n=int(input())
    if(abs(n-low)<=abs(high-n)):
        print('A')
        low=n
    else:
        print('B')
        high=n
    t=t-1
