n=int(input())

m=int(input())

def fun(n,m,summ=1):

    if m!=0:

        summ=fun(n,m-1,summ*n)

    
    return summ
print(fun(n,m))