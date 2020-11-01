l=int(input())
n=int(input())
while n>0:
    w,h=[int(x) for x in input().split()]
    if h>=l or w>=l:
        if (w==l and h==l) or (w==h):
            print('ACCEPTED')
    if w>=l:
        if (h>l or h==l) and w!=h:
            print('CROP IT')
        if h<l:
            print('UPLOAD ANOTHER')
    elif h>=l:
        if (w>l or w==l) and w!=h:
            print('CROP IT')
        if w<l:
            print('UPLOAD ANOTHER')
    elif h<l or w<l:
        print('UPLOAD ANOTHER')
    elif (w>l and h>l) and w==h:
        print('ACCEPTED')

    n=n-1
