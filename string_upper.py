a = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M',
     'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
b = input()
c = []
for i in a:
    c.append({i, a[i]})

'''
for i, j in enumerate(b):
    if i == 0:
        c += a[b[i]]
    elif b[i+1] == " " or i+1 > len(b)-1:
        c += a[b[i]]
    elif b[i-1] == " ":
        c += a[b[i]]
    else:
        c += b[i]'''
print(c)
