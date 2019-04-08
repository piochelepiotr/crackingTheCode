def delete_value(head, x):
    if head and head.next:
        if head.next.value == x:
            head.next = head.next.next
            delete_value(head, x)
        else:
            delete_value(head.next, x)
    return head
