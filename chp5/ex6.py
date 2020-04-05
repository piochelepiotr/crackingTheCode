def conversion(n1, n2):
    n = n1 ^ n2
    # count number of 1 in n
    c = 0
    while n != 0:
        n = n & (n-1) # this clears the least significant bit
        c += 1
    return c

def conversion_easy(n1, n2):
    n = n1 ^ n2
    # count number of 1 in n
    c = 0
    while n != 0:
        if n & 1:
            c += 1
        n >>= 1
    return c
