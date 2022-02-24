arr = [1, 2, 3, +6, 5, -6, -5, 6, -3, 5, 26, 16, 5, 16, 3, 1, 65, 1, 6, 5, 1]
b = 34
n = len(arr)
c = {}
for i in range(n - 1):
    s = {}
    for j in range(i + 1, n):
        x = b - (arr[i] + arr[j])
        if x in s:
            print(x, arr[i], arr[j])
        else:
            s[arr[j]] = 1

#alternative


def threeSum(self, nums):

    nums.sort()
    N, result = len(nums), []
    for i in range(N):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = nums[i] * -1
        s, e = i + 1, N - 1
        while s < e:
            if nums[s] + nums[e] == target:
                result.append([nums[i], nums[s], nums[e]])
                s = s + 1
                while s < e and nums[s] == nums[s - 1]:
                    s = s + 1
            elif nums[s] + nums[e] < target:
                s = s + 1
            else:
                e = e - 1
    return result
