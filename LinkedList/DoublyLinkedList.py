class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = None

    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtStart(data)
            return
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insertAt(self, pos, data):
        if pos < 0 or pos > self.len():
            raise IndexError("Invalid position")
        elif pos == 0:
            self.insertAtStart(data)
        elif pos == self.len():
            self.insertAtEnd(data)
        else:
            temp = self.head
            new_node = Node(data)
            for i in range(pos - 1):
                temp = temp.next
            temp.next.prev = new_node
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node

    def remove(self, data):
        if self.head is None:
            raise ValueError("List is empty!")
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            while temp:
                if temp.data == data:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
                    break
                temp = temp.next

    def contains(self, data):
        if self.head:
            temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def display(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def len(self):
        count = 0
        if self.head:
            temp = self.head
            while temp:
                count += 1
                temp = temp.next
        return count


dl = DoublyLinkedList()
dl.insertAtStart(10)
dl.insertAtStart(5)
dl.insertAtStart(3)
dl.insertAtEnd(15)
dl.insertAtEnd(20)
dl.insertAt(4, 18)
dl.remove(20)
dl.remove(10)
dl.remove(15)
dl.display()
print()
print(dl.contains(18))
print("Size: ", dl.len())
print(f"Head: {dl.head.data} Tail: {dl.tail.data}")
