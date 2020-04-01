import stack

def sort_stack(s):
    tmp_stack = stack.Stack()
    while s.size() > 0:
        x = s.pop()
        while tmp_stack.size() > 0 and tmp_stack.peek() > x:
            s.push(tmp_stack.pop())
        tmp_stack.push(x)
    return tmp_stack
