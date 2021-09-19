n = int(input())
a = [[int(input()) for _ in range(n)] for _ in range(n)]


def swap(c, d):
    return d, c


print('--------------')
for i in a:
    for j in i:
        print(j, end=' ')
    print()

for i in range(n):
    for j in range(i+1, n):
        a[i][j], a[j][i] = swap(a[i][j], a[j][i])


for i in a:

    l = 0
    r = n-1
    while l < r:
        i[l], i[r] = swap(i[l], i[r])
        l += 1
        r -= 1

print('--------------')

for i in a:
    for j in i:
        print(j, end=' ')
    print()
