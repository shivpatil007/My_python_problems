a=input()
b=input()
if a[0] not in b:
    print(-1)

for i in range(len(a),-1,-1):
    
    if a[:i] in b:
        
        z=b.index(a[:i])
        if z!=len(b)-1:
            if z-1<len(b[z:]):
                print(z)
            else:
                print(len(b[z:]))
            break
        else:
            x=0
            if b[x]==a[i]:
                while a[i]==b[x]:
                    x+=1
                    i+=1
                
                
            
            














'''for i,j in enumerate(b):
    k=0
    if a[k]==j:
        x=0
        l=i
        while k<len(a) and l<len(b) and a[k] == b[l] :
            x+=1
            k+=1
            l+=1
        if x>count:
            count=x
            '''

