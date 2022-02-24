a = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

stack = list(range(len(a)))
while len(stack) > 1:
    i, j = stack.pop(), stack.pop()
    if a[j][i]:
        stack.append(i)
    elif a[i][j]:
        stack.append(j)

if not stack:
    print("NO CEELEBRITY")
else:
    k = 0
    potensial_celebrity = stack.pop()
    for i in range(len(a)):
        if a[potensial_celebrity][i]:
            print("NO CEELEBRITY")
            k = 1
            break
        if i != potensial_celebrity and not a[i][potensial_celebrity]:
            print("NO CEELEBRITY")
            k = 1
            break

    if k == 0:
        print("celebrity is=", potensial_celebrity)
