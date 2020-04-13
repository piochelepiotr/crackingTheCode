def permutations(s):
    if len(s) == 1:
        return set(s)
    perm = permutations(s[1:])
    r = set()
    for p in perm:
        for i in range(len(s)):
            r.add(p[0:i] + s[0] + p[i:len(s)-1])
    return r
