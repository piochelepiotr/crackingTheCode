import collections

def robot_path(grid):
    # paths hold the path to go to the init point
    n_row = len(grid)
    n_columns = len(grid[0])
    paths = [[None for c in range(n_columns)] for r in range(n_row)]
    queue = collections.deque()
    queue.append((0, 0, "START", []))
    while len(queue) > 0 and paths[n_row -1][n_columns-1] is None:
        r,c,d,p = queue.popleft()
        if r < 0 or c < 0 or r >= n_row or c >= n_columns or grid[r][c] or paths[r][c]:
            continue
        paths[r][c] = p + [d]
        p = paths[r][c]
        queue.append((r-1,c, "UP", p))
        queue.append((r+1,c, "DOWN", p))
        queue.append((r,c-1, "LEFT", p))
        queue.append((r,c+1, "RIGHT", p))
    return paths[n_row-1][n_columns-1]
