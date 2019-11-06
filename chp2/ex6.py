import linked_list

class Stack:
    def __init__(self):
        self.l = None

    def pop(self):
        if self.l is None:
            return None
        x = self.l.value
        self.l = self.l.next
        return x
    
    def push(self, x):
        self.l = linked_list.Node(x, self.l)


def is_palindrome2(head):
    first_half = Stack()
    slow_runner = head
    fast_runner = head
    while fast_runner:
        fast_runner = fast_runner.next
        if fast_runner:
            fast_runner = fast_runner.next
            first_half.push(slow_runner.value)
        slow_runner = slow_runner.next

    while slow_runner:
        if slow_runner.value != first_half.pop():
            return False
        slow_runner = slow_runner.next
    return True

print(is_palindrome2(linked_list.from_list([7, 1, 5, 1, 7])))
print(is_palindrome2(linked_list.from_list([7, 1, 5, 1, 8])))

def _reverse_list(L):
    r = None
    while L is not None:
        r = linked_list.Node(L.value, r)
        L = L.next
    return r


def is_palindrome(L):
    return _reverse_list(L) == L

