def power_set(s):
    n = len(s)
    sub_sets = []
    for i in range(pow(2, n)):
        sub_set = set()
        for j, x in enumerate(s):
            if (1 << j) & i:
                sub_set.add(x)
        sub_sets.append(sub_set)
    return sub_sets
