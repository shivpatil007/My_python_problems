# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root) -> int:

        def myfun(root):
            if not root:
                return 0

            l = myfun(root.left)
            r = myfun(root.right)

            max1 = max(max(l, r) + root.val, root.val)
            max2 = max(max1, l + r + root.val)

            myfun.res = max(max2, myfun.res)
            return max1

        myfun.res = float('-inf')
        myfun(root)
        return myfun.res