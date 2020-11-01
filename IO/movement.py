n=int(input())
p=n
i=5
step=0
while n>0:
    p=p-i-step
    step=step+1
    i=i-1
    n=p
print(step)
