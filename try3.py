

def fun(x, a, output, n):
    if x == '':
        for i in a:
            output = fun(x+i, a, output, n)
    elif len(x) < n:
        for i in a[x[-1]]:
            output = fun(x+i, a, output, n)

    else:

        output += 1
    return output


n = int(input())
a = {'a': ['e'], 'e': ['a', 'i'], 'i': [
    'a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
if n == 0:
    print(0)
else:
    print(fun('', a, 0, n))
