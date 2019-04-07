import linked_list


# the 1 last is the last one
def k_last_element(head, k):
    node = head
    for i in range(k):
        if node is None:
            return None
        node = node.next
    klast = head
    while node is not None:
        klast = klast.next
        node = node.next
    return klast.value
