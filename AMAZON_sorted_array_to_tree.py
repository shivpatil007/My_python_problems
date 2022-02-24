a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def myfun(a):
    x = len(a) // 2

    root = Node(a[x])
    if x != 0:
        root.left = myfun(a[:x])
    if x + 1 < len(a):
        root.right = myfun(a[x + 1:])
    return root


COUNT = [10]


def print2DUtil(root, space):
    if root is None:
        return

    space += COUNT[0]
    print2DUtil(root.right, space)
    print()
    for _ in range(COUNT[0], space):
        print(end=" ")
    print(root.data)
    print2DUtil(root.left, space)


def print2D(root):
    print2DUtil(root, 0)


print2D(myfun(a))
