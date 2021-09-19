def myfun(n,curr,value):
    if curr==n:
        value[0]+=1
        return
    elif curr>n:
        return
    else:
        myfun(n,curr+1,value)
        myfun(n,curr+2,value)

value=[0]
myfun(30,0,value)
print (value[0])