
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.size += 1
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        else:
            return self.front.data


queue = LinkedListQueue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size)
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Is empty:", queue.is_empty())
