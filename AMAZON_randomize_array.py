ans = [
    646, 51, 56, 5, 6161, 51, 1, 16, 136, 1, 365, 6, 1, 6, 1, 1, 6153, 51, 1,
    6163, 51, 31, 61, 31, 1351, 3, 51, 354
]
import random
for i in range(len(ans) - 1, 0, -1):  # start from end
    j = random.randrange(0, i + 1)  # generate random index
    ans[i], ans[j] = ans[j], ans[i]  # swap
print(ans)