def is_prime(n):

    if n == 1:
        return False

    i = 2

    while i*i <= n:

        if n % i == 0:

            return False
        i += 1

    return True


def fun(i, j, target):

    ans = []
    z = [x for x in range(i, j) if is_prime(x) == True]
    for i, j in enumerate(z):
        for k in z[i+1:]:
            if k-j == target:
                ans.append([j, k])
                break
    return ans


if __name__ == "__main__":
    z = []
    a = int(input())
    b = int(input())
    target = 6
    ans = fun(a, b+1, target)
    print(ans)
