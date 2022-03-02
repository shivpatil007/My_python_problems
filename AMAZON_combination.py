#comination of list without itertools and without repetition

lst = [1, 2, 3]


def combination(lst, n):
    if n == 0:
        return [[]]
    return [
        pre + [lst[i]] for i in range(len(lst))
        for pre in combination(lst[i + 1:], n - 1)
    ]


res = []
for i in range(len(lst) + 1):
    res.extend(combination(lst, i))
print(res)

#alternate methodd

result = [[]]
for num in lst:
    result += [i + [num] for i in result]
print(result)