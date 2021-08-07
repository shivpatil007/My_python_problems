a=input()
b=int(a[:2])
c=int(a[3:])

if c>12:
    
    if b<5:
        if c<b*10:
            x=(b*10)-c
        else:
            x=60-c
            x+=(b+1)*10
    else:
        vfdv=5
print(x)