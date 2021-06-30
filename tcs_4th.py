import re
a = input()
b = re.findall(r'\d+', a)
print(b)
for i in b:
    if '9' in i:
        b.remove(i)
b = [int(x) for x in b]
print(b)
