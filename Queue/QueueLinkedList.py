class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        else:
            temp = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return temp.data

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        return self.head.data

    def display(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
        print()

    def isEmpty(self):
        return self.head is None

    def delete(self):
        self.head = None
        self.tail = None


ql = QueueLinkedList()
ql.enqueue(10)
ql.enqueue(20)
ql.enqueue(30)
ql.dequeue()
print("Peek element: ", ql.peek())

ql.display()

