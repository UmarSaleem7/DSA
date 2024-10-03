class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.previous = None


class Doubly_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Display(self):
        if self.head is None:
            return print('List is Empty')
        current = self.head
        print('[', end='')
        while True:
            if current is None:
                break
            print(current.data, end='')
            if current.next is not None:
                print(end=', ')
            current = current.next
        print(']')

    # Insertion
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        return

    def insert_at_tail(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return


def main():
    linked_list = Doubly_LinkedList()
    linked_list.insert_at_tail(3)
    linked_list.Display()
    linked_list.insert_at_head(2)
    linked_list.Display()
    linked_list.insert_at_head(1)
    linked_list.Display()
    linked_list.insert_at_tail(4)
    linked_list.Display()


main()
