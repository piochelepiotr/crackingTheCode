import collections

def root_between(graph, i, j):
    visited = [False] * len(graph.nodes)
    to_visit = collections.deque()
    to_visit.append(i)
    while len(to_visit) > 0:
        x = to_visit.popleft()
        if visited[x]:
            continue
        visited[x] = True
        if x == j:
            return True
        _,neighbours = graph.nodes[x]
        to_visit.extend(neighbours)
