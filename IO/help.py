s=input('')
v=0
l=['A','E','I','O','U','Y']
for ch in range(len(s)-1):
    if s[ch].isalpha()==True:
        if s[ch] in l:
            print('Invalid')
            v=v+1
            break
    if (s[ch].isnumeric()==True) and (s[ch+1].isnumeric()==True):
        p=int(s[ch])+int(s[ch+1])
        if p%2!=0:
            print('Invalid')
            v=v+1
            break
    if (s[ch].isnumeric()==False) and (s[ch].isalpha()==False):
        continue
if v!=1:
    print('Valid')
