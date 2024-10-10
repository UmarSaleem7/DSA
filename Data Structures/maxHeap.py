class maxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def insert(self, num):

        self.heap.append(num)
        self.heapify_up(len(self.heap)-1)

    def deque(self):
        root = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        largest = i
        if l < len(self.heap) and self.heap[l] > self.heap[i]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)