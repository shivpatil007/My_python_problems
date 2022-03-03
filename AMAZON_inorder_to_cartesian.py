"""
https://www.techiedelight.com/construct-cartesian-tree-from-inorder-traversal/
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


COUNT = [10]


def print2DUtil(root, space):

    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for _ in range(COUNT[0], space):
        print(end=" ")
    print(root.data)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):

    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


inorder = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]


def myfun(inorder, start, end):
    if not inorder[start:end]: return None
    minn = inorder.index(min(inorder[start:end]))
    root = Node(inorder[minn])
    root.left = myfun(inorder, start, minn)
    root.right = myfun(inorder, minn + 1, end)
    return root


print2D(myfun(inorder, 0, len(inorder)))
