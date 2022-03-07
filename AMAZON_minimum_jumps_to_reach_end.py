def myfun(a, n):
    if n <= 1: return 0
    if a[0] == 0: return -1
    maxreach = a[0]
    jump = 1
    step = a[0]
    for i in range(1, n):
        if i == n - 1: return jump
        maxreach = max(maxreach, i + a[i])
        step -= 1
        if not step:
            jump += 1
            if i >= maxreach:
                return -1
            step = maxreach - i
    return -1


a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
n = len(a)
print(myfun(a, n))
