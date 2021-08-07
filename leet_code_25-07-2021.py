n=int(input())
count=0
for i in range(n+1):
    x=bin(i)[2:]
    c=0
    for j in range(len(x)-1):
        
        if x[j]=="1" and x[j+1]=="1":
            
            c=1
            break
    if c==0:
        
        count+=1
print(count)