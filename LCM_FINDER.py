n = int(input())
m = int(input())

'''a, b = {}, {}

while n != 1:

    for i in range(2, n+1):
        if n % i == 0:
            n //= i
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
            break

while m != 1:

    for i in range(2, m+1):
        if m % i == 0:
            m //= i
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
            break
summ = 1
for i, value in a.items():
    summ *= i**max(value, b[i]) if i in b else (i**a[i])

for i, value_ in b.items():
    if i not in a:
        summ *= i**value_

print(summ)
'''


def hcf(num1, num2):
    if num2 == 0:
        return num1
    return hcf(num2, num1 % num2)


def lcm(num1, num2):
    return (num1*num2)/hcf(num1, num2)


print(lcm(n, m))
