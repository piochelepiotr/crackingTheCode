def is_balanced(t):
    balanced,_ = is_balanced_and_height(t)
    return balanced

def is_balanced_and_height(t):
    if t is None:
        return True, 0
    b_left, n_left = is_balanced_and_height(t.left)
    b_right, n_right = is_balanced_and_height(t.right)
    return b_left and b_right and abs(n_left-n_right) <= 1, max(n_left, n_right) + 1
