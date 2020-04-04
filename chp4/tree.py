class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        left = str(self.left) if self.left else ""
        right = str(self.right) if self.right else ""
        return "[{} {} {}]".format(left, self.value, right)

    def build_parents(self, parent=None):
        self.parent = parent
        if self.left:
            self.left.build_parents(self)
        if self.right:
            self.right.build_parents(self)

    def find_in_search_tree(self, v):
        if self.value == v:
            return self
        if v > self.value:
            if self.right:
                return self.right.find_in_search_tree(v)
            return None
        if v < self.value:
            if self.left:
                return self.left.find_in_search_tree(v)
            return None
