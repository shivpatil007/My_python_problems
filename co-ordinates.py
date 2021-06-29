a = input()
b = input()
x = a[-1]
y = b[-1]
c = {}
d = {}
for i in a[:-1]:
    if i not in c.keys():
        c[i] = 1
    else:
        c[i] += 1

for i in b[:-1]:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

if x == 's':
    x = "South"
else:
    x = "North"

if y == 'w':
    y = "West"
else:
    y = "East"

print(str(max(c.values()) - min(c.values())) + ' ' + x +
      " " + str(max(d.values()) - min(d.values())) + ' ' + y)
