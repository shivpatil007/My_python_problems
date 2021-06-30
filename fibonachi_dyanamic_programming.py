
def fibo(n, a):
    if a[n] != None:
        return a[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibo(n-1, a)+fibo(n-2, a)
    a[n] = result
    return result


if __name__ == "__main__":

    n = int(input())
    a = [None]*(n+1)
    result = fibo(n, a)
    print(result)
