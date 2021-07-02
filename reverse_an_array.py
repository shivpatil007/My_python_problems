a = [5, 5, 2, 6, 4, 20, 66, 5, 25, 3, 34, 0, 25, 6, 31, 4, 8]
i = 0
j = len(a)
print(j)
if j % 2 == 0:
    j -= 1
    while i < len(a)/2 and j >= len(a)/2:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1
else:
    j -= 1
    while i < int(len(a)/2) and j >= int(len(a)/2)+1:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1
print(a)
