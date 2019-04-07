def is_permutation(str1, str2):
    occurences = {}
    for c in str1:
        try:
            occurences[c] += 1
        except KeyError:
            occurences[c] = 1
    for c in str2:
        try:
            occurences[c] -= 1
        except KeyError:
            return False
    for c in occurences:
        if occurences[c] != 0:
            return False
    return True
