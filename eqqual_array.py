def make_equal(a, n):
    for i in range(n):
        while (a[i] % 2 == 0):
            a[i] = a[i]/2

        while (a[i] % 3 == 0):
            a[i] = a[i]/3
    print(a)
    for i in range(n):
        if a[i] != a[0]:
            return False
    return True


num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
if make_equal(arr, num) == True:
    print("Yes")
else:
    print("NO")
