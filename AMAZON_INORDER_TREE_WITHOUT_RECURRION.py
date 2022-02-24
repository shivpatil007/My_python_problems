class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)

            current = current.left

        elif stack:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right

        else:
            break


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)