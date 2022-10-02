class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        new_node = Node(data)
        # if self.head is None:
        #     self.head = new_node
        #     return
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

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
        else:
            temp = self.head
            flag = False
            while temp:
                if temp.data == data:
                    flag = True
                    break
                prev = temp
                temp = temp.next
            if flag:
                prev.next = temp.next
            else:
                raise Exception("List has no such item!")

    def contains(self, data):
        if self.head:
            temp = self.head
            while temp:
                if temp.data == data:
                    return True
                temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def len(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


sl = SinglyLinkedList()
sl.insertAtEnd(5)
sl.insertAtEnd(15)
sl.insertAtStart(3)
sl.insertAtStart(1)
sl.insertAt(4, 20)
sl.insertAt(1, 2)
sl.insertAt(3, 4)
sl.insertAt(5, 6)
sl.insertAt(0, 0)
sl.remove(20)
sl.remove(0)
sl.remove(6)
sl.insertAt(5, 10)
print(sl.contains(15))
sl.display()
print(f"size: {sl.len()}")
