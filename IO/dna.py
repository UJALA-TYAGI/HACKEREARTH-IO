ch=input('')
s=''
for i in ch:
    if i not in 'ATGC':
        s='Invalid Input'
        break
    if i=='C':
        s+='G'
    if i=='G':
        s+='C'
    if i=='T':
        s+='A'
    if i=='A':
        s+='U'
print(s)




#or you can use this

#b=input()
#a="GCTA";c="CGAU"
#try:print(''.join([c[a.index(i)]for i in b]))
#except:print("Invalid Input")

#a,c="GCTA","CGAU"
#try:print(''.join([c[a.index(i)]for i in input()]))
#except:print("Invalid Input")
