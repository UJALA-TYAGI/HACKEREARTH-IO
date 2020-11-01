for i in range(0,int(input())):
    s1,s2=[x for x in input().split()]
    l1=[]
    l2=[]
    for (x,y) in zip(s1,s2):
        l1.append(x)
        l2.append(y)
    if sorted(l1)==sorted(l2):
        print('YES')

    else:
        print('NO')
