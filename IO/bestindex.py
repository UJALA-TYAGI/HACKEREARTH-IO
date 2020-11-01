import math
n=int(input())
arr=list(map(int,input().split()))
ary=[*range(0,n+1)]
max =-10000000
for i in range(1,n):
    ary[i]=arr[i-1]+ary[i-1]
for i in range(0,n):
    k=i
    j=2
    while k+j<n:
            k=j+k
            j+=1
    ss=ary[k+1]-ary[i]
    if ss>max:
        max=ss
print(ss)




#N=int(input())
#ns=[int(n) for n in input().split()]
#k = 2
#start = 1
#while start<=N:
#    start += k
#    k += 1
#    start-= k - 1
#    k -= 2
#    s = sum(ns[:start])
#    print(s)
#    ms = s
#    for i in range(1, N):
#        s -= ns[i - 1]
#        print('hello',s)
#        if start <N:
#            s += ns[start]
#            print('if',s)
#            start += 1
#        else:
#            k -= 1
#            s -= sum(ns[N - k:N])
#            print('else',s)
#    start -= k
#print(s)
#print(ms)
#if s > ms:
#    ms = s
#    print(ms)
