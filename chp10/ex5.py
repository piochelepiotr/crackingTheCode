def sparse_search(array, x):
    first = 0
    last = len(array) - 1
    while last - first > 0:
        m = (last + first) // 2
        while m > 0 and array[m] == "":
            m -= 1
        if array[m] == "":
            first = (last + first) // 2 + 1
        elif x < array[m]:
            last = m - 1
        elif x > array[m]:
            first = m + 1
        else:
            return m
    return last
