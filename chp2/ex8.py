def find_loop(L):
    nodes = set()
    while L is not None:
        if L in nodes:
            return L
        nodes.add(L)
        L = L.next
    return None
