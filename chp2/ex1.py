import linked_list


def remove_dups(head):
    if head is None:
        return None
    s = set()
    node = head
    s.add(node.value)
    while node.next is not None:
        if node.next.value in s:
            node.next = node.next.next
        else:
            s.add(node.next.value)
            node = node.next
    return head


assert linked_list.to_list(remove_dups(linked_list.from_list([1, 2, 3, 4, 5]))) == [
    1,
    2,
    3,
    4,
    5,
]
assert linked_list.to_list(remove_dups(linked_list.from_list([1, 2, 1, 4, 5]))) == [
    1,
    2,
    4,
    5,
]
