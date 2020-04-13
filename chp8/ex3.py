# we have f(i) = A[i] >= i. It is False, False, False, then it starts to be always True,
# this is the definition of dichotomie

def magic_index(a):
    def f(x):
        return a[x] >= x
    i = 0
    j = len(a) - 1
    while j-i != 0:
        h = (j+i) >> 1
        if f(h):
            # we know magic index is between i and h (included)
            j = h
        else:
            # we know magic index is between h+1 and j
            i = h+1
    if a[j] == j:
        return j
    return None
