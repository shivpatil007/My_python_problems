def myfun(a):
    from collections import defaultdict
    m = defaultdict(int)
    count = -1
    for i in a:
        m[i] += 1
        count = max(m[i], count)
    print(count)


a = [1, 3, 4, 5]
myfun(a)