for i in range(0,int(input())):
    n=int(input())
    p=2*n
    ch="*"
    for x in range(0,n):
        p=p-2
        str=''
        for c in range(p):
            str=str+"#"
        print(ch+str+ch)
        ch=ch+"*"


#t=int(input())
#for j in range(t):

#    x=int(input())
#    y='*'
#    z='#'
#    for i in range(1,x+1):
#        print(y*i,end='')
#        print((z*(2*(x-i))),end='')
#        print(y*i)
