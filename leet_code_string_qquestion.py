'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
'''


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
