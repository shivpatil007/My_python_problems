a = 'fddfvf'
c = ''
max = 0
for i, j in enumerate(a):
    c += j
    if c[::-1] == a[i+1:i+len(c)+1]:
        max = len(c)

print(max)
