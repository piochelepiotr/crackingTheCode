import collections

def build_order(projects, dependencies):
    children_map = {}
    parent_map = {}
    visited = {}
    for p in projects:
        children_map[p] = []
        parent_map[p] = []
        visited[p] = False
    for parent, child in dependencies:
        children_map[parent].append(child)
        parent_map[child].append(parent)

    processing = collections.deque()
    for p in parent_map:
        if len(parent_map[p]) == 0:
            processing.append(p)

    order = []

    while len(processing) > 0:
        p = processing.popleft()
        if visited[p]:
            continue
        visited[p] = True
        order.append(p)
        for x in children_map[p]:
            processing.append(x)

    if len(order) < len(projects):
        return []
    return order
