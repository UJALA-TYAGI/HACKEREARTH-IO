t=int(input())
while t>0:
    count=0
    lst=['a','e','i','o','u']
    n=int(input())
    s=input('')
    if len(s)==n:
        for i in range(1,len(s)):
            if s[i] in lst:
                if s[i-1] not in lst:
                    count=count+1
    print(count)
    t=t-1
