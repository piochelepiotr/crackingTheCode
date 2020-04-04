def find_successor(node):
    if node.right:
        node = node.right
        while not node.left is None:
            node = node.left
        return node
    while node.parent and node.parent.right is node:
        node = node.parent
    node = node.parent
    return node
