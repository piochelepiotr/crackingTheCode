from collections import Counter


# maybe not great to use counts after all
def permutations(s):
    counts = Counter(s)
    def perm(c):
        if len(c) == 0:
            return set([""])
        r = set()
        for i in c:
            sub_c = c.copy()
            sub_c.subtract([i])
            if sub_c[i] == 0:
                del sub_c[i]
            perms = perm(sub_c)
            for p in perms:
                r.add(i + p)
        return r
    return perm(counts)
