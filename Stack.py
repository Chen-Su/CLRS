class Stack:
    def __init__(self):
        self.data = []
        self.top = 0

    def push(self, val):
        self.data.append(val)
        self.top += 1

    def pop(self):
        if self.top == 0:
            print('Stack is empty.')
            return
        self.top -= 1
        res = self.data[self.top]
        self.data.pop(self.top)
        return res

    def top(self):
        if self.top == 0:
            print('Stack is emtpy.')
            return
        return self.data[self.top-1]

s = Stack()
s.push(1)
s.push(2)
print(s.data)
print(s.pop())
print(s.pop())
print(s.pop())
