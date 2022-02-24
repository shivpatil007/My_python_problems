def myfun(arr, dep, n):
    plat = 1
    res = 1
    i = 1
    j = 0
    arr.sort()
    dep.sort()
    while i < n and j < n:
        if arr[i] <= dep[j]:
            plat += 1
            i += 1
        elif arr[i] >= dep[j]:
            plat -= 1
            j += 1
        res = max(res, plat)

    return res


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(myfun(arr, dep, len(arr)))
