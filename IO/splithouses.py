n=int(input())
s=input('')
if len(s)==n:
    a=0
    b=0
    atpos=s.find('H')
    spos=s.find('H',atpos)
    a=abs(spos-atpos)
    for i in range(0, len(s)-1) :
        if s[i]=='H' and s[i]==s[i+1]:
            b=b+1


    if (a==1 or b>=1) and n!=1:
        print('NO')
    else:
        print('YES')
        print(s.replace('.','B'))
