class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.que = [None for _ in range(size)]
        self.front = -1
        self.rear = -1

    def __str__(self):
        val = [str(x) for x in self.que]
        return ' '.join(val)

    def enqueue(self, data):
        if self.isFull():
            raise IndexError("Queue is full!")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.que[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.que[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        elif self.front == self.rear:
            temp = self.que[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.que[self.front]
            self.que[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        return self.que[self.front]

    def display(self):
        if self.isEmpty():
            print("Queue is empty!")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.que[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.que[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.que[i], end=" ")
            print()

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.dequeue()
cq.enqueue(60)

print(cq)
cq.display()
