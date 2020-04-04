def check_binary_search_tree(t):
    ok,_,_ = check_binary_search_tree_and_min_max(t)
    return ok

def check_binary_search_tree_and_min_max(t):
    if t is None:
        return True, None, None
    max_x = t.value
    min_x = t.value
    left_ok, min_left, max_left = check_binary_search_tree_and_min_max(t.left)
    right_ok, min_right, max_right = check_binary_search_tree_and_min_max(t.right)
    ok = left_ok and right_ok
    if min_left:
        if max_left > t.value:
            ok = False
        min_x = min(min_x, min_left)
        max_x = max(max_x, max_left)
    if min_right:
        if min_right < t.value:
            ok = False
        min_x = min(min_x, min_right)
        max_x = max(max_x, max_right)
    return ok, min_x, max_x
