def bit_swap_32(n):
    keep_even = 0x55555555
    keep_odd = 0xAAAAAAAA
    return ((n >> 1) & keep_even) | ((n << 1) & keep_odd)
