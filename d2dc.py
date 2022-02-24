n = int(input())
a = list(map(int, input().split()))
b = []
c = []
d = []
for i in a:
    if i % 2 == 0:
        if i % 5 == 0:
            b.append(i)
        else:
            c.append(i)
    else:
        d.append(i)
b.sort(reverse=True)

print(b+c[::-1]+d)
