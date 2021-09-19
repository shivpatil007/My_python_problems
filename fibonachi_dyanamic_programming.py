
def fibo(n, a):
    if a[n] != None:
        return a[n]
    result = 1 if n in [1, 2] else fibo(n-1, a)+fibo(n-2, a)
    a[n] = result
    return result


if __name__ == "__main__":

    n = int(input())
    a = [None]*(n+1)
    result = fibo(n, a)
    print(result)
    print(a)
