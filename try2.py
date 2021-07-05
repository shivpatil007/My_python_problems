

def fun(x, a, output, n):

    if len(x) < n:
        for i in a[x[-1]]:
            output += fun(x+i, a, output, n)

    else:
        print(x)
        output += 1
    return output


z = 0
n = int(input())
result = 0
a = {'a': ['e'], 'e': ['a', 'i'], 'i': [
    'a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
if n == 0:
    print(0)
else:
    for i in a.keys():

        result += (fun(i, a, result, n))
print(result)
