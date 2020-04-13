def parenthesis(n):
    return p(n*2, 0)

def p(n, s):
    if n == 0:
        if s == 0:
            return [""]
        else:
            return []
    r = []
    if s > 0:
        ri = p(n-1, s-1)
        for x in ri:
            r.append(")" + x)
    if s+1 <= n-1:
        ri = p(n-1, s+1)
        for x in ri:
            r.append("(" + x)
    return r
