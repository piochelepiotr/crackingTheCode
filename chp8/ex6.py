def interm(i, j):
    all = set([0, 1, 2])
    all.remove(i)
    all.remove(j)
    return all.pop()

def hanoi(n):
    towers = [[i for i in range(n)], [], []]
    def move(origin, to, i):
        if i == 1:
            towers[to].append(towers[origin].pop())
            return
        t = interm(origin, to)
        towers[t].append(towers[origin].pop())
        move(origin, to, i-1)
        towers[to].append(towers[t].pop())
    move(0, 2, n)
    return len(towers[0]), len(towers[1]), len(towers[2])
