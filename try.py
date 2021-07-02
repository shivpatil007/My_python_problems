def is_prime(n):

    if n == 1:
        return False

    i = 2

    while i*i <= n:

        if n % i == 0:

            return False
        i += 1

    return True


a = [5, 66, 5, 5, 5, 2, 3, 4]
print(a)
b = a.reverse()
print(b)
print(a)
