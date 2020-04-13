def coins(n):
    c = [25, 10, 5, 1]
    d = {}
    for x in c:
        d[x] = [-1 for i in range(n+1)]
    def coins_left(c, n):
        if len(c) == 1:
            # only ones left
            return 1
        if d[c[0]][n] != -1:
            return d[c[0]][n]
        s = 0
        c2 = c[1:]
        n2 = n
        while n2 >= 0:
            s += coins_left(c2, n2)
            n2 -= c[0]
        d[c[0]][n] = s
        return s
    return coins_left(c, n)
