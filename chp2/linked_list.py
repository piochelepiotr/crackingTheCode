class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        return to_list(self) == to_list(other)

    def __repr__(self):
        return str(to_list(self))


def from_list(L):
    node = None
    n = len(L)
    for i in range(n - 1, -1, -1):
        node = Node(L[i], node)
    return node


def to_list(node):
    L = []
    while node is not None:
        L.append(node.value)
        node = node.next
    return L
