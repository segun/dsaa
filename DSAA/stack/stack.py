class Stack(object):
    def __init__(self, size=0, top=-1):
        self.size = size
        self.top = top
        self.stack = []

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            return self.stack[self.top]

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            value = self.stack[self.top]
            self.top = self.top - 1
            return value

    def push(self, data):
        if self.is_full():
            raise ValueError("Stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(data)
