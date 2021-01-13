# this doesn't work actually, we forget some of the fields
def search_matrix(mat, x):
    rows = len(mat)
    columns = len(mat[0])
    # first, find on the where between two numbers on the diag the number is
    first = 0
    last = min(rows, columns)
    while last - first > 1:
        m = (last + first) // 2
        if x >= mat[m][m]:
            first = m
        else:
            last = m
    # now, we have one row and one column where the number can be.
    # try row first
    first_c = first
    last_c = columns
    while last_c - first_c > 0:
        m = (last_c + first_c) // 2
        if x > mat[first][m]:
            first_c = m+1
        elif x < mat[first][m]:
            last_c = m-1
        else:
            return (first, m)

    if mat[first][first_c] == x:
        return first, first_c

    # now, do column
    first_r = first
    last_r = rows
    while last_r - first_r > 0:
        m = (last_r + first_r) // 2
        if x > mat[m][first]:
            first_r = m+1
        elif x < mat[m][first]:
            last_r = m-1
        else:
            return (m, first)

    if mat[first_r][first] == x:
        return first_r, first

    return -1
