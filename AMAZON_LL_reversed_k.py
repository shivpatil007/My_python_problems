class Node:

    def __init__(self, data) -> None:
        self.val = data
        self.next = None


def reverse(head, k):
    count, node = 0, head
    while node and count < k:
        node = node.next
        count += 1
    if count < k: return head
    new_head, prev = reverse_count(head, count)
    head.next = reverse(new_head, k)
    return prev


def reverse_count(head, count):
    prev, curr, nxt = None, head, head
    while count > 0:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count -= 1
    return (curr, prev)


def print_LL(head):
    while head:
        print(head.val, end=" ")
        head = head.next


head = Node(3)
head.next = Node(6)
head.next.next = Node(9)
head.next.next.next = Node(15)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next.next = Node(1)
head.next.next.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next.next.next.next = Node(8)

print_LL(head)
print()
print_LL(reverse(head, 3))
