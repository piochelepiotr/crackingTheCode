import linked_list

def partition(head, x):
    first = head.value
    second = head.next.value
    if first > second:
        first, second = second, first
    high = linked_list.Node(second, None)
    low = linked_list.Node(first, high)
    head = head.next.next
    while head:
        if head.value >= x:
            high.next = linked_list.Node(head.value, None)
            high = high.next
        else:
            low = linked_list.Node(head.value, low)
        head = head.next
    return low

L = linked_list.from_list([1, 5, 10, 3, 4, 6])
l = partition(L, 5)
print(l)
