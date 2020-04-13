from collections import deque

def paint_fill(screen, pos, color):
    n_r = len(screen)
    n_c = len(screen[0])
    visited = [[False for i in range(n_c)] for j in range(n_r)]
    to_visit = deque()
    to_visit.append(pos)
    (r,c) = pos
    old_color = screen[r][c]
    while len(to_visit) > 0:
        (r, c) = to_visit.popleft()
        if r >= n_r or c >= n_c or c < 0 or r < 0 or visited[r][c] or screen[r][c] != old_color:
            continue
        visited[r][c] = True
        to_visit.append((r+1, c))
        to_visit.append((r-1, c))
        to_visit.append((r, c+1))
        to_visit.append((r, c-1))
    for r in range(n_r):
        for c in range(n_c):
            if visited[r][c]:
                screen[r][c] = color
