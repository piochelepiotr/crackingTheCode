import stack

class SetOfStacks:
    def __init__(self, max_height):
        self.max_height = max_height
        self.current_stack = 0
        self.stacks = [stack.Stack()]

    def push(self, x):
        if self.stacks[self.current_stack].size() == self.max_height:
            self.stacks.append(stack.Stack())
            self.current_stack += 1
        self.stacks[self.current_stack].push(x)

    def pop(self):
        if self.stacks[self.current_stack].size() == 0:
            if self.current_stack == 0:
                raise Exception("empty stack")
            self.current_stack -= 1
        return self.stacks[self.current_stack].pop()

    def pop_at(self, n):
        if n > self.current_stack or n < 0:
            raise Exception("invalid stack id")
        if self.stacks[n].size() == 0:
            raise Exception("empty stack")
        x = self.stacks[n].pop()
        if self.stacks[n].size() == 0:
            del self.stacks[n]
            self.current_stack -= 1
        return x


