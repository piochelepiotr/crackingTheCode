class MinStack:
    def __init__(self):
        self.elements = []
    
    def add(self, x):
        new_min = x
        if self.elements:
            _,m = self.elements[-1]
            new_min = min(m, new_min)
        self.elements.append((x, new_min))

    def pop(self):
        if not self.elements:
            raise Exception("can't pop element from empty stack")
        x,_ = self.elements[-1]
        del self.elements[-1]
        return x

    def min(self):
        if not self.elements:
            raise Exception("can't pop element from empty stack")
        _,m = self.elements[-1]
        return m
