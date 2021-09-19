def is_prime(n):

    if n == 1:
        return False

    i = 2

    while i ** 2 <= n:

        if n % i == 0:

            return False
        i += 1

    return True


print(is_prime(56))
