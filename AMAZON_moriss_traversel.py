class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def myfun(root):
    curr = root
    while curr is not None:
        if curr.left is None:
            yield curr
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right is not curr:
                pre = pre.right

            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                yield curr
                curr = curr.right


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
for i in myfun(root):
    print(i.val, end=" ")