class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    # Insertion
    def insert_at_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        # Below code is also correct
        # if self.head is None:
        #     self.head = new_node
        #     return
        # temp = self.head
        # self.head = new_node
        # self.head.next = temp
        # del temp

    def insert_at_tail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def insert_after(self, key, val):
        newnode = Node(val)
        current_node = self.head
        if current_node is None:
            print("List is Empty")
            return
        while current_node:
            if current_node.data == key:
                temp = current_node.next
                current_node.next = newnode
                newnode.next = temp
                return
            current_node = current_node.next
        return print(f'Key NOT Found')

    def insert_before(self, key, val):
        newnode = Node(val)
        current_node = self.head
        if current_node.data == key:
            self.insert_at_head(val)
            return
        previous_node = None
        while current_node:
            if current_node.data == key:
                previous_node.next = newnode
                newnode.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
        return print(f'Key NOT Found')

    # Search
    def search(self, key):
        current_node = self.head
        while True:
            if current_node is None:
                print("Element Not Exist")
                return
            elif current_node.data == key:
                print("Element Found")
                return
            current_node = current_node.next

    # Display
    def Display(self):
        if self.head is None:
            print("Linked list is Empty")
            return
        current_node = self.head
        print('[', end='')
        while True:
            if current_node is None:
                break
            else:
                print(current_node.data, end='')
                if current_node.next is not None:
                    print(', ', end='')
                current_node = current_node.next
        print(']')

    # Update
    def Update(self, key, val):
        current = self.head
        while current:
            if current.data == key:
                current.data = val
                return
            current = current.next
        return print(f'Key value NOT Found')

    # Removal
    def remove_from_head(self):
        temp = self.head
        if temp is None:
            return f"Linked List is Empty"
        self.head = temp.next
        del temp

    def remove_from_tail(self):
        current = self.head
        if current is None:
            return f'Linked List is Empty'
        if current.next is None:
            self.head = None
            return
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        # below code also correct
        # if current.next is None:
        #     del current
        #     self.head = None
        #     return
        # temp = None
        # while current:
        #     if current.next is None:
        #         temp.next = None
        #         del current
        #         return
        #     temp = current
        #     current = current.next

    def remove_after(self, key):
        current = self.head
        if current is None:
            return print('List is Empty')
        while current:
            if current.data == key and current.next is None:
                return print(f'Element does not exist after Key: {key}')
            if current.data == key and current.next is not None:
                temp = current.next
                current.next = temp.next
                del temp
                return
            current = current.next
        return print('Key NOT Found')

    def remove_before(self, key):
        current = self.head
        if current is None or current.next is None:
            return print(f'List is Empty or Contain  only one Element')
        if current.data == key:
            return print(f'Nothing to remove before First Element')
        if current.next.data == key:
            temp = self.head
            self.head = temp.next
            del temp
            return
        previous = None
        while current.next and current.next.data != key:
            previous = current
            current = current.next
        if current.next:
            previous.next = current.next
        else:
            print('Key NOT Found')
        return


def main():
    linkedlsit = LinkList()
    print('----------insert at tail----------')
    linkedlsit.insert_at_tail(3)
    linkedlsit.Display()
    print('----------insert at head----------')
    linkedlsit.insert_at_head(1)
    linkedlsit.Display()
    print('----------insert at tail----------')
    linkedlsit.insert_at_tail(2)
    linkedlsit.Display()
    print('----------insert after 3----------')
    linkedlsit.insert_after(3, 4)
    linkedlsit.Display()
    print('----------insert before 1----------')
    linkedlsit.insert_before(1, 0)
    linkedlsit.Display()
    print('----------search element 4----------')
    linkedlsit.search(4)
    print('----------update element 3----------')
    linkedlsit.Update(3, -1)
    linkedlsit.Display()
    print('----------remove from head----------')
    linkedlsit.remove_from_head()
    linkedlsit.Display()
    print('----------remove from tail----------')
    linkedlsit.remove_from_tail()
    linkedlsit.Display()
    print('----------remove after 1----------')
    linkedlsit.remove_after(1)
    linkedlsit.Display()
    print('----------remove before 4----------')
    linkedlsit.remove_before(4)
    linkedlsit.Display()


main()
