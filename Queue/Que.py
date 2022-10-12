class Queue:
    def __init__(self):
        self.que = []

    def __str__(self):
        val = [str(x) for x in self.que]
        return ' '.join(val)

    def enqueue(self, item):
        self.que.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Queue is empty!")
        return self.que.pop(0)

    def peek(self):
        if self.que:
            return self.que[0]
        else:
            raise ValueError("Queue is empty!")

    def size(self):
        return len(self.que)

    def isEmpty(self):
        return len(self.que) == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.peek())
print(q)
