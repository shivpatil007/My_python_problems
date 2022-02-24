a = [5, 7, 1, 2, 8, 4, 3]
c = 12
b = {}
for i in a:
    if c - i in b:
        print(b[c - i], i)
    else:
        b[i] = i
