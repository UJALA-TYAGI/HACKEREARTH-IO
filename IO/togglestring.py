s=input('')
str=''
for ch in s:
    if ch.isupper():
        str=str+ch.lower()
    elif ch.islower():
        str=str+ch.upper()
print(str)
