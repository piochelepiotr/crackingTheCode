def flip_bit(s):
    max_l = 0
    current_l = 0
    next_l = 0
    for x in s:
        if x == '1':
            current_l += 1
            next_l += 1
        else:
            max_l = max(max_l, current_l)
            current_l = next_l + 1
            next_l = 0
    max_l = max(max(max_l, current_l), next_l)
    return max_l
