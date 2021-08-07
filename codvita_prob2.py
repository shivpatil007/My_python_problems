n,m=map(int,input().split(" "))
sum=0
prev=-1
next=-1
for _ in range(n):
    a=list(map(int,input().split(" ")))
    x=a.index(max(a))
    if x!=prev:
        sum+=max(a)
        prev=x
    else:
        a.pop(x)
        sum+=max(a)
        prev=a.index(max(a))
print(sum)