class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def lenght_of_list(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def push_at_the_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


if __name__ == "__main__":
    llist = LinkList()
    llist.push_at_the_front(1)
    llist.push_at_the_front(2)
    llist.push_at_the_front(3)
    llist.push_at_the_front(4)
    llist.push_at_the_front(5)
    llist.push_at_the_front(5)
    llist.print_list()
    lllist = LinkList()
    lllist.push_at_the_front(1)
    lllist.push_at_the_front(2)
    lllist.push_at_the_front(3)
    lllist.print_list()

    llist.head = llist.reverse_list()
    lllist.head = llist.reverse_list()

    if llist.lenght_of_list() > lllist.lenght_of_list():
        cur1 = llist.head
        cur2 = lllist.head
        x = 0
        while cur2 != None:
            data = cur1.data + cur2.data + x
            if data > 10:
                cur1.data = data % 10
            x = int(data / 10)
            cur1 = cur1.next
            cur2 = cur2.next
        if x != 0:
            while cur1 != None:
                cur1.data += (x % 10)
                x = int(x / 10)
                cur1 = cur1.next
