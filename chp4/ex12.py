def paths_with_sum(t, s, started=False):
    if t is None:
        return 0
    paths = 0
    if not started:
        # if we don't start the path at this node
        paths += paths_with_sum(t.left, s, False)
        paths += paths_with_sum(t.right, s, False)

    # if the path is already started or we choose to start it at this node
    if t.value == s:
        paths += 1
    paths += paths_with_sum(t.left, s-t.value, True)
    paths += paths_with_sum(t.right, s-t.value, True)
    return paths
