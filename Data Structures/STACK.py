class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            val = self.top.data
            self.top = self.top.next
            self.size -= 1
            return val

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.top.data


def main():
    stack = Stack()
    print(stack.is_empty())
    stack.push(5)
    stack.push(2)
    print('Pop element:', stack.pop())
    stack.push(7)
    stack.push(9)
    print('Element at peek:', stack.peek())
    print('Size of stack:', stack.size)
    print(stack.is_empty())


main()
