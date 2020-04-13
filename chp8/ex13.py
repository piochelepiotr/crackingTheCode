# this is without the strict ordering, it's 2^n in space inefficient
def highest_stack_not_strict(boxes):
    boxes_left = pow(2, len(boxes))-1 # bit i at 1 indicates that box i is still here
    m = [-1 for i in range(pow(2, len(boxes)))]
    def stack_rec(boxes_left, w, h, d):
        if m[boxes_left] != -1:
            return m[boxes_left]
        max_height = 0
        for i, (b_w, b_h, b_d) in enumerate(boxes):
            if not ((1 << i & boxes_left) and b_w <= w and b_h <= h and b_d <= d):
                continue
            max_height = max(max_height, b_h + stack_rec(boxes_left & ~(1 << i), min(b_w, w), min(b_h, h), min(b_d, d)))
        m[boxes_left] = max_height
        return max_height
    return stack_rec(boxes_left, 100000000, 10000000000, 10000000000)

# with strict ordering, it's much simpler

def highest_stack(boxes):
    boxes.sort(reverse=True, key=lambda b: b[2])
    m = [-1 for i in range(len(boxes)+1)]
    def stack_rec(base_index, box_index):
        (w, h, d) = boxes[box_index]
        if not (base_index is None):
            (b_w, b_h, b_d) = boxes[base_index]
            if w >= b_w or h >= b_h: # no need to check for depth, it's sorted
                # we can't add the box, so return 0
                return 0
        if m[box_index] != -1:
            return m[box_index]
        max_height = 0
        for i in range(box_index+1, len(boxes)):
            max_height = max(max_height, stack_rec(box_index, i))
        m[box_index] = max_height + h
        return max_height + h
    return stack_rec(None, 0)
