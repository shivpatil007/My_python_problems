
m=int(input())
n=int(input())
strik=[1]*n
strik[0]=0
strik[1]=0

for i in range(2,int(n**0.5)+1):
    if strik[i]!=0:
        strik[i*i:n:i]=[0]*((n-1-i*i)//i+1)
a = [int(str(i)[::-1]) for i in range(m,n) if strik[i]==1]

x=max(a)+1
d=[1]*x
d[0]=0
d[1]=0
for i in range(2,int(x**0.5)+1):
    if d[i]!=0:
        d[i*i:x:i]=[0]*((x-1-i*i)//i+1)

print([int(str(i)[::-1]) for i in a if d[i]==1])
