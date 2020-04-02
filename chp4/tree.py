class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        left = str(self.left) if self.left else ""
        right = str(self.right) if self.right else ""
        return "[{} {} {}]".format(left, self.value, right)
