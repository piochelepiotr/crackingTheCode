def merge_lists(l1, l2):
    if len(l2) > len(l1):
        l1, l2 = l2, l1
    for i, x in enumerate(l2):
        l1[i].extend(x)
    return l1

def values_by_depth(t):
    if t == None:
        return []
    x = [[t.value]]
    x.extend(merge_lists(values_by_depth(t.left), values_by_depth(t.right)))
    return x
