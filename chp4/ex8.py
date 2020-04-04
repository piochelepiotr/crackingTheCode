def first_common_ancestor(n1, n2):
    d1 = depth(n1)
    d2 = depth(n2)
    if d1 > d2:
        d1, d2 = d2, d1
        n1, n2 = n2, n1
    for i in range(d2 - d1):
        n2 = n2.parent
    while n1 != n2:
        n2 = n2.parent
        n1 = n1.parent
    return n1

def depth(n):
    if n is None:
        return 0
    return 1 + depth(n.parent)
