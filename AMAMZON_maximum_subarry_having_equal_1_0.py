a = [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
max_len = 0
dic = {}
count = 0
for i in range(len(a)):
    n = a[i]
    if not n: count -= 1
    elif n == 1: count += 1
    if count in dic:
        max_len = max(max_len, i - dic[count])
    else:
        dic[count] = i

print(max_len)
