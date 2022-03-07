from lib2to3.pgen2.pgen import DFAState

a = [10, 1, 2, 7, 6, 1, 5]
target = 8


def dfs(nums, target, ind, path, res):
    if target <= 0:
        if target == 0:
            res.append(path)
        return
    for i in range(ind, len(nums)):
        if i > ind and nums[i] == nums[i - 1]:
            continue
        dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)


res = []
ind = 0
dfs(sorted(a), target, ind, [], res)
print(res)
