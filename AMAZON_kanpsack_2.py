from random import randrange

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
dp = [0] * (W + 1)
for i in range(W + 1):
    for j in range(n):
        if wt[j] < i:

            dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

print(dp)
print(dp[W])
