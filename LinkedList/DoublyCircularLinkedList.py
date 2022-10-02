class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = self.head

    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtStart(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = self.tail

    def insertAt(self, pos, data):
        if pos < 0 or pos > self.len():
            raise IndexError("Invalid position!")
        elif pos == 0:
            self.insertAtStart(data)
        elif pos == self.len():
            self.insertAtEnd(data)
        else:
            new_node = Node(data)
            temp = self.head
            for i in range(pos - 1):
                temp = temp.next
            new_node.prev = temp
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node

    def remove(self, data):
        if self.head is None:
            raise Exception("List is empty!")
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            temp = self.head
            while True:
                if temp.data == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return 0
                temp = temp.next
                if temp == self.head:
                    raise Exception("List has not such element!!")

    def contains(self, data):
        if self.head:
            temp = self.head
            while True:
                if temp.data == data:
                    return True
                temp = temp.next
                if temp == self.head:
                    return False
        return False

    def display(self):
        if self.head:
            temp = self.head
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break

    def len(self):
        count = 0
        if self.head:
            temp = self.head
            while True:
                count += 1
                temp = temp.next
                if temp == self.head:
                    break
        return count


dcl = DoublyCircularLinkedList()
dcl.insertAtStart(5)
dcl.insertAtStart(3)
dcl.insertAtEnd(10)
dcl.insertAt(1, 4)
dcl.insertAt(3, 7)
dcl.remove(3)
dcl.remove(10)
dcl.remove(5)
# dcl.remove(55)
dcl.insertAtStart(1)
dcl.insertAtEnd(10)
dcl.insertAt(2, 5)
print(dcl.contains(45))

dcl.display()
print()

print(f"Size: {dcl.len()}  Head: {dcl.head.data}  Tail: {dcl.tail.data}")

# For debugging purpose
print(dcl.head.prev.data, dcl.tail.next.data)
