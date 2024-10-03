class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def is_empty(self):
        if self.front == -1:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print('Circular Queue is Full')
            return
        else:
            if self.front == -1:
                self.front = self.rear = 0
                self.queue[self.front] = data
            else:
                self.rear += 1
                if self.rear == self.size:
                    self.rear = 0
                self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            return f'Circular Queue is Empty'
        elif self.front == self.rear:
            x = self.queue[self.front]
            self.front = self.rear = -1
            return x
        else:
            x = self.queue[self.front]
            self.front += 1
            if self.front == self.size:
                self.front = 0
            return x

    def display(self):
        if self.is_empty():
            print('Circular Queue is Empty')
            return
        elif self.rear > self.front:
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=' ')
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear+1):
                print(self.queue[i], end=' ')
            print()


def main():
    cq = CircularQueue(5)
    cq.display()
    print(cq.is_empty())
    print(cq.is_full())
    print(cq.dequeue())
    cq.enqueue(2)
    cq.enqueue(5)
    cq.display()
    print(cq.is_empty())
    cq.enqueue(3)
    cq.enqueue(1)
    cq.display()
    print(cq.dequeue())
    cq.display()
    cq.enqueue(4)
    cq.enqueue(6)
    cq.display()
    cq.enqueue(7)
    print(cq.is_full())


main()
