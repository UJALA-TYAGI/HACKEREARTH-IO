#from collections import Counter
#def cc(a,b):
#    p = Counter(a)
#    q = Counter(b)
#    print(sum((q-p).values())+sum((p-q).values()))



#n  = int(input())
#for _ in range(n):
#    a = input()
#    b = input()
#    cc(a,b)
from collections import Counter
n  = int(input())
for _ in range(n):
    s1= input()
    s2= input()
    p = Counter(s1)
    q = Counter(s2)
    print(sum((q-p).values())+sum((p-q).values()))

#t=int(input())
#i=[]
#while t>0:
#    b=0
#    a=0
#    s1=input('')
#    s2=input('')
#    lst1=sorted(list(s1))
#    lst2=sorted(list(s2))
#    if lst1!=lst2:
#        if(len(lst1)!=len(lst2)):
#            b=abs(len(lst1)-len(lst2))
#        for (ch1,ch2) in zip(lst1,lst2):
#            if(ch1==ch2):continue
#            lst1.remove(ch1)
#            lst2.remove(ch2)
#            a=a+2
#        i.append(a+b)
#    t=t-1
#print(*i,sep="\n")
