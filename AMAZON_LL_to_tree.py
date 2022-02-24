class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head):

        def helper(head):
            if not head: return None

            slow = fast = head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None

            root = TreeNode(slow.val)
            # base case
            if head == slow:
                return root

            root.left = helper(head)
            root.right = helper(slow.next)

            return root

        return helper(head)