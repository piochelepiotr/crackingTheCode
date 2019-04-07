def set_to_0(mat):
    rows_to_set = set()
    columns_to_set = set()
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                rows_to_set.add(i)
                columns_to_set.add(j)
    for i in rows_to_set:
        for j in range(m):
            mat[i][j] = 0

    for j in columns_to_set:
        for i in range(n):
            mat[i][j] = 0
