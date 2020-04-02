import tree

def build_search_tree(l):
    if len(l) == 0:
        return None
    m = len(l)//2
    return tree.Node(l[m], build_search_tree(l[:m]), build_search_tree(l[m+1:]))
