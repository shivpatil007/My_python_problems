class Solution:

    def solve(self, matrix):
        matrix = sorted(matrix, key=lambda x: (x[0], -x[1]))
        n = len(matrix)

        heights = [float("inf")] * (n + 1)
        heights[0] = float("-inf")
        res = 0

        for box in matrix:
            cur_w, cur_h = box
            index = self.insert_index(heights, cur_h)

            if heights[index] >= cur_h:
                heights[index] = cur_h
            res = max(res, index)
        return res

    def insert_index(self, arr, this_h):
        l = 0
        r = len(arr) - 1
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            cur_h = arr[m]
            if cur_h < this_h:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res + 1


ob = Solution()
matrix = [[12, 12], [10, 10], [6, 6], [5, 10]]
print(ob.solve(matrix))