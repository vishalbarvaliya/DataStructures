class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head = new_node
        self.tail.next = self.head

    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtStart(data)
            return
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def insertAt(self, pos, data):
        if pos < 0 or pos > self.len():
            raise Exception("Invalid position!")
        elif pos == 0:
            self.insertAtStart(data)
            return
        elif pos == self.len():
            self.insertAtEnd(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def remove(self, data):
        if self.head is None:
            raise Exception("List is empty!")
        elif self.head.data == data:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            temp = self.head
            flag = False
            while True:
                if temp.data == data:
                    flag = True
                    break
                prev = temp
                temp = temp.next
                if temp == self.head:
                    break
            if flag:
                prev.next = temp.next
                if prev.next == self.head:
                    self.tail = prev
            else:
                raise Exception("List has no such item!")

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
        print()

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


scl = SinglyCircularLinkedList()
scl.insertAtStart(10)
scl.insertAtStart(5)
scl.insertAtEnd(20)
scl.insertAt(0, 2)
scl.insertAt(3, 15)
scl.insertAt(1, 3)
scl.remove(2)
scl.remove(20)
print(scl.contains(31))
scl.display()
print()
print(f"size: {scl.len()}\nHead: {scl.head.data}\nTail: {scl.tail.data}")
