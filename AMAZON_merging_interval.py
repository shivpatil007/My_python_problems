a = [[6, 8], [1, 9], [2, 4], [4, 7]]

    a = sorted(a, key=lambda x: x[0])
    res = [a.pop(0)]
    i = 0
    while a:
        comp = res[-1]
        if comp[0] < a[i][0] and comp[1] > a[i][1]:
            a.pop(i)
        elif comp[1] > a[i][0] and comp[1] < a[i][1]:
            res[-1][1] = a[i][1]
            a.pop(0)
        else:
            res.append(a.pop(0))
    print(res)
