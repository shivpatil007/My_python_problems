def fun(m, n, a):
    if str(m)+','+str(n) in a.keys():
        return a[str(m)+','+str(n)]
    if m == 0 or n == 0:
        result = 0
    elif m == 1 and n == 1:
        result = 1
    else:
        result = fun(m-1, n, a) + fun(m, n-1, a)
    a[str(m)+','+str(n)] = result

    return result


m = int(input())
n = int(input())
count = 0
a = {}
result = fun(m, n, a)
print(result)
