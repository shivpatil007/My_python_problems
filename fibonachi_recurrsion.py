
def fibo(n):

    if n == 1 or n == 2:
        result = 1
    else:
        result = fibo(n-1)+fibo(n-2)

    return result


if __name__ == "__main__":

    n = int(input())

    result = fibo(n)
    print(result)
