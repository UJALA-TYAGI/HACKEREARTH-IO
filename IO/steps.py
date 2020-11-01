n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
# sort both the lists together
a,b = (list(l) for l in zip(*sorted(zip(a,b))))
a_min = a[0] #min value
i = 0
while(i < n):
    while(a[i] > a_min):
        a[i] -= b[i]
        count += 1
    if a[i] == a_min:
        i += 1
        continue
    if a[i] < b[i]:
        count = -1
        break
    if a[i] < a_min: #rare case
        a_min = a[i]
        i = 0
        continue
    i+= 1
print(count)

#n=int(input())
#a=list(map(int,input().split()))
#b=list(map(int,input().split()))
#x=a.index(min(a))
#s=0
#for i in range(len(a)):
#    if (i==x) or (a[i]==a[x]):
#        continue
#    while (a[i]!=min(a)) and :
#        if (a[i]>b[i]) and ((a[i]-b[i])>=a[x]):
#            a[i]=a[i]-b[i]
#            s+=1


#if s==0:
#    print('-1')
#else:
#    print(s)
