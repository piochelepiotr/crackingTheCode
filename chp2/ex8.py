def is_in_list(L, v):
    for x in L:
        if x is v:
            return True
    return False


def find_loop(L):
    nodes = []
    while L is not None:
        if is_in_list(nodes, L):
            return L
        nodes.append(L)
        L = L.next
    return None
