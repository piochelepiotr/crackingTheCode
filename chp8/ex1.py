def stairs_possibilities(n):
    mem = [0 for i in range(max(n+1, 3))]
    mem[0] = 1
    mem[1] = 1
    mem[2] = 2
    def get_possibilites(i):
        if mem[i] != 0:
            return mem[i]
        mem[i] = get_possibilites(i-1) + get_possibilites(i-2) + get_possibilites(i-3)
        return mem[i]
    return get_possibilites(n)
