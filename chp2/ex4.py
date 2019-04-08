import linked_list


def partition(head, x):
    low = None
    high = None
    L = head
    while L:
        if L.value >= x:
            high = linked_list.Node(L.value, high)
        else:
            low = linked_list.Node(L.value, low)
        L = L.next
    return low, high
