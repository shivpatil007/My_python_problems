n=int(input())
m=int(input())


def myfun(m,curr):
    
    if curr==m:
        value[0]+=1
        return
    elif curr>m:
        return
    if curr!=curr+((curr+int(m/2))%m):
        myfun(m,curr+((curr+int(m/2))%m))
    myfun(m,curr+1)
    

value=[0]
myfun(m,n)
print(value[0])

