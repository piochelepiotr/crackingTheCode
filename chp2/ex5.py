import linked_list


def sum_lists(l1, l2, carry=0):
    if l1 is None and l2 is None:
        return None

    def expand_list(l):
        if l is None:
            return 0, None
        else:
            return l.value, l.next
    l1_value, l1_next = expand_list(l1)
    l2_value, l2_next = expand_list(l2)
    s = divmod(l1_value + l2_value + carry, 10)
    passed_carry = 0
    if s >= 10:
        s -= 10
        passed_carry = 1
    return linked_list.Node(s, sum_lists(l1_next, l2_next, passed_carry))
