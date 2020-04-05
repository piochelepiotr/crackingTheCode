def insertion(n, m, i, j):
    mask = ~(((1 << (j - i + 1)) - 1) << i)
    return (m << i) | (n & mask)
