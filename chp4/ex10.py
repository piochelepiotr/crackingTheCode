def is_sub_tree(t1, t2):
    while not t1.parent is None:
        t1 = t1.parent
    while not t2.parent is None:
        t2 = t2.parent
    return t1 is t2
