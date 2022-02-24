s = 'shiv'

res = []


def myfun(s, answer):
    if len(s) == 0:
        res.append(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        myfun(s[:i] + s[i + 1:], answer + ch)


myfun(s, '')
print(res)
print(set(res))