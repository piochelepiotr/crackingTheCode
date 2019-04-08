import linked_list


def _reverse_list(L):
    r = None
    while L is not None:
        r = linked_list.Node(L.value, r)
        L = L.next
    return r


def is_palindrome(L):
    return _reverse_list(L) == L
