def _intersection_node(parent_list, child_list):
    L = parent_list
    while L is not None:
        if L is child_list:
            return child_list
        L = L.next
    return None


def intersection_node(l1, l2):
    return _intersection_node(l1, l2) or _intersection_node(l2, l1)
