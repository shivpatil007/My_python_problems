# There are a row of n houses, each house can be painted with one of the k colors.
#  The cost of painting each house with a certain color is different.
#   You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x k cost matrix.
#  For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the
#  cost of painting house 1 with color 2, and so on… Find the minimum cost to paint all houses.

# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
#  Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

cost = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
n = len(cost)
if n == 0:
    print(0)
elif n == 1:
    print(min(cost[0]))
k = len(cost[0])
for i in range(1, n):
    for j in range(k):
        prehouse = cost[i - 1]
        cost[i][j] += min(prehouse[:j] + prehouse[j + 1:])

print(min(cost[-1]))
