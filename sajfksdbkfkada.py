s = -1


def myfun(a, i, j, summ):
    m = 4
    n = 4
    if i == m-1 and j == n-1:
        if s < summ+a[i][j]:
            s = summ+a[i][j]
        return
    summ += a[i][j]
    if 0 <= i+1 < m:
        myfun(a, i+1, j, summ)
    if 0 <= j+1 < n:
        myfun(a, i, j+1, summ)


a = [[1, 2, 3, 5], [9, 6, 1, 3], [
    6, 4, 3, 1], [9, 3, 3, 4]]
myfun(a, 0, 0, 0)
print(max(s))
