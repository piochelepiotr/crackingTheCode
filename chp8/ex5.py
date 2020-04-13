def rec_multiply(n1, n2):
    if n2 == 0:
        return 0
    if n2 & 1:
        return n1 + (rec_multiply(n1, n2 >> 1) << 1)
    else:
        return rec_multiply(n1, n2 >> 1) << 1

