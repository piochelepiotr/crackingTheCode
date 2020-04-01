class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, x):
        self.elements.append(x)

    def pop(self):
        if not self.elements:
            raise Exception("empty stack")
        x = self.elements[-1]
        del self.elements[-1]
        return x

    def size(self):
        return len(self.elements)

    def peek(self):
        if not self.elements:
            raise Exception("empty stack")
        return self.elements[-1]
