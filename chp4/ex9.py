def bst_sequence(t):
    if t is None:
        return [[]]
    possible_arrays = []

    left = bst_sequence(t.left)
    right = bst_sequence(t.right)
    if t.left and t.right:
        possible_arrays = merge(left, right) + merge(right, left)
    elif t.left:
        possible_arrays = left
    else:
        possible_arrays = right

    possible_arrays = merge([[t.value]], possible_arrays)
    return possible_arrays

def merge(first, second):
    x = []
    for a in first:
        for b in second:
            x.append(a + b)
    return x
