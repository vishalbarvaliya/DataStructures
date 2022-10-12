class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        val = [str(x) for x in self.stack[::-1]]
        return ' '.join(val)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return ValueError("Stack is empty!")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return ValueError("Stack is empty!")

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        pass

    def delete(self):
        self.stack = []


st = Stack()

st.push(20)
st.push(15)
st.push(5)

print(st)
print(st.pop())
print("Peek: ", st.peek())

