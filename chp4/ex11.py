from random import randrange

def random_node(t):
    n = t.get_size()
    return t.random(randrange(n))

class RandomNode:
    def __init__(self, value):
        self.size = 1
        self.left = None
        self.right = None
        self.value = value

    def get_size(self):
        return self.size

    # insert keeps the tree as balanced as possible
    def insert(self, x):
        self.size += 1
        if self.left is None:
            self.left = RandomNode(x)
            return
        if self.right is None:
            self.right = RandomNode(x)
            return
        left_size = self.left.get_size()
        right_size = self.right.get_size()
        if right_size > left_size:
            self.right.insert(x)
            return
        self.left.insert(x)

    def random(self, n):
        left_size = 0
        right_size = 0
        if self.left:
            left_size = self.left.get_size()
        if self.right:
            right_size = self.right.get_size()
        if n < left_size:
            return self.left.random(n)
        if n > left_size:
            return self.right.random(n - left_size - 1)
        return self
