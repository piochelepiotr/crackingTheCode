import stack

class MyQueue:
    def __init__(self):
        self.in_stack = stack.Stack()
        self.out_stack = stack.Stack()

    def push(self, x):
        self.in_stack.push(x)

    def pull(self):
        if self.out_stack.size() == 0:
            if self.in_stack.size() == 0:
                raise Exception("empty queue")
            while self.in_stack.size() > 0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
