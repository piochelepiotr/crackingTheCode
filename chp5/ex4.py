def next_higher(n):
    # we need to make it bigger, but not to big.
    # if we change a 0 to 1 to make it bigger, we will need to change a 1 to 0. We can't change anything left from the 1, without making it smaller, so the change will have to be right of the 1. So we need to change the 0 that is the most to the right, but with a 1 at the left of it
    # and then, we need to put all the ones right to the 1 we switched to the extreme right. To make the number as small as possible
    #    100001111000
    # -> 100011111000
    # -> 100010000111
    c = n
    c0 = 0
    c1 = 0
    while ((c & 1) == 0) and c != 0:
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    if c0 + c1 == 0:
        raise Exception("no bigger number with same number of 1")

    p = c0 + c1 # position of rightmost non-trailing zero
    n |= (1 << p) # flip rightmost non-trailing zero
    n &= ~((1 <<p) -1) # clear all bits right of p
    n |= ((1 << (c1 -1)) - 1) # insert c1 -1 zeros on the right
    return n

def next_lower(n):
    c = n
    c0 = 0
    c1 = 0

    while (c & 1) == 1:
        c >>= 1
        c1 += 1

    while ((c & 1) == 0) and c != 0:
        c >>= 1
        c0 += 1

    if c == 0:
        raise Exception("no lower number with same number of 1")
    
    p = c0 + c1 # position of rightmost non-trailing 1
    n &= ((~0) << (p + 1)) # clear p and right of p
    mask = (1 << (c1 + 1)) - 1 # mask of c1 + 1 ones
    n |= (mask << (c0 - 1))
    return n

