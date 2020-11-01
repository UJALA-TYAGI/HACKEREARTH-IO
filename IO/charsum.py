s=input('')
a=[]
n=[]
sum=0
for i in range(1,27):
    a.append(chr(i+96))
    n.append(i)
for ch in s:
    if ch in a:
        pos=a.index(ch)
        sum=sum+int(n[pos])
print(sum)
