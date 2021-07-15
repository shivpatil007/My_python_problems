def minSetSize(self, arr):

    a = {}
    x = int(len(arr)/2)

    for i in arr:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    c = a.values()
    sum = 0
    j = 0
    c.sort(reverse=True)
    if len(c) == 1:
        return 1
    for i in c:
        if sum + i <= x:
            sum += i
            j += 1

    if j == 48:
        j += 1
    return j
