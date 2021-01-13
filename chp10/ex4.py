
def get_element_at(listy, i):
    if i >= len(listy):
        return -1
    return listy[i]

def search_no_size(listy, x):
    first = 0
    last = 1
    # first find first and last
    while True:
        e = get_element_at(listy, last)
        if e == -1 or e >= x:
            break
        first = last
        last *= 2

    # now, binary search
    while last - first > 0:
        m = (last + first) // 2
        e = get_element_at(listy, m)
        if e == -1 or x < e:
            last = m-1
        else:
            first = m + 1
    return last
