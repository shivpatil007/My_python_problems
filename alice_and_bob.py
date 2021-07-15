import time


def fun(s, order):
    a={}
    b=''
    for i in s:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1

    for i in order:
        if i in a:
            b+=i*a[i]
            a.pop(i)
    for i, value in a.items():
        b += i * value
    return b