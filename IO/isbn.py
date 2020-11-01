n=input('')
sum=0
if len(n)!=10:
    print('Illegal ISBN')
    exit()
else:
    p=int(n)
    for i in range(1,11):
        sum+=(p%10)*i
        p=int(p/10)
        print(p)
print(sum)
if int(sum)%11==0:
    print('Legal ISBN')
else:
    print('Illegal ISBN')
