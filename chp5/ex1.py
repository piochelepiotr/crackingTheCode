def insertion(n, m, i, j):
    mask = (~0 << (j + 1)) + ((1 << i) - 1)
    return (m << i) + (n & mask)


print(insertion(1 << 10, 19, 2, 6))
