s=input('')
p=[0,0]
for ch in s:
    if ch=='L':
        p[0]=p[0]-1
    elif ch=='R':
        p[0]=p[0]+1
    elif ch=='U':
        p[1]=p[1]+1
    elif ch=='D':
        p[1]=p[1]-1
print(*p,sep=" ")
