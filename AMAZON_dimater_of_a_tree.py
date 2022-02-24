class Node:

    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:

    def __init__(self) -> None:
        self.h = 0


def diameter(root, height):
    if not root:
        height.h = 0
        return 0
    lh = Height()
    rh = Height()
    ldiameter = diameter(root.left, lh)
    rdiameter = diameter(root.right, rh)
    height.h = max(lh.h, rh.h) + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
height = Height()
print(diameter(root, height))
