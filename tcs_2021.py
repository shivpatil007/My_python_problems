
def fun(n):
    a = ''

    while(n > 1):
        max = 0
        for i in range(9, 2, -1):
            if n % i == 0:

                max = i
                break
        if max == 0:
            return 'Not possible'
        n /= max
        a += str(max)

    return a[::-1]


n = int(input())
print(fun(n))
