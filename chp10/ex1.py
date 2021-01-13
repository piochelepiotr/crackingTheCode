def merge_sorted(a, b, len_a):
    ia, ib = len_a -1, len(b) -1
    i = len_a + len(b) -1
    while i >= 0:
        if ib < 0 or ia >= 0 and a[ia] >= b[ib]:
            a[i] = a[ia]
            ia -= 1
            i -= 1
        else:
            a[i] = b[ib]
            ib -= 1
            i -= 1
