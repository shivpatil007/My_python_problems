
n = int(input())
p = int(input())
a = [[0 for i in range(50)] for _ in range(n+1)]

for j in range(1, n+1):
    i = 1
    a[j][0] = 5000*j
    while i < 50:
        a[j][i] = a[j][i-1]+5000+i
        if a[j][i] == p:
            print(j)
            break
        i += 1
