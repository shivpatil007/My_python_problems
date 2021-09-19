a=input()
i=0
while a[i]==' ':
    i+=1
s=''
if a[i]=='h':
    s+='http://'
    i+=4
elif a[i]=='f':
    s+='ftp://'
    i+=3
while a[i]+a[i+1]!='ru':
    s+=a[i]
    i+=1
s+='.ru/'
i+=2
s+=a[i:]
print(s)



