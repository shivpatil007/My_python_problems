a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
b = input()
c = {}
for i in b:
    if i not in c.keys():
        c[i] = 1
    else:
        c[i] += 1
flag = 1
for i in c:
    if c[i] == a[i]:
        pass
    else:
        flag = 0
        break
if flag == 1:
    print("yes")
else:
    print("No")
