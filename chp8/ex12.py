def queens():
    n = 8
    taken_col = [False for i in range(n)]
    taken_diag_up = [False for i in range(n*2)]
    taken_diag_down = [False for i in range(n*2)]
    return queens_r(0, taken_col, taken_diag_up, taken_diag_down, n, [])

def queens_r(r, taken_col, taken_diag_up, taken_diag_down, n, result):
    if r == n:
        return [format_result(result)]
    results = []
    for c in range(n):
        d_up = r-c+n
        d_down = c-r+n
        if taken_col[c] or taken_diag_up[d_up] or taken_diag_down[d_down]:
            continue
        taken_col[c] = True
        taken_diag_up[d_up] = True
        taken_diag_down[d_down] = True
        results.extend(queens_r(r+1, taken_col, taken_diag_up, taken_diag_down, n, result + [c]))
        taken_col[c] = False
        taken_diag_up[d_up] = False
        taken_diag_down[d_down] = False
    return results


def format_result(res):
    return [["Q" if c == i else ".." for i in range(len(res))] for c in res]

def print_board(board):
    print()
    for r in board:
        for x in r:
            print(x, end='')
        print()
