class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        val = []
        while temp:
            val.append(str(temp.data))
            temp = temp.next
        return " ".join(val)

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp.data
        else:
            raise ValueError("Stack is empty!")

    def peek(self):
        if self.head:
            return self.head.data
        else:
            raise ValueError("Stack is empty!")


stl = StackLinkedList()
stl.push(20)
stl.push(15)
stl.push(5)
print(stl.pop())
print(stl)
print(stl.peek())



