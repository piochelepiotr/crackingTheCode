def has_uniq_characters(str):
    characters = set()
    for c in str:
        if c in characters:
            return False
        characters.add(c)
    return True


def has_uniq_characters_without_datastructure(str):
    for i in range(len(str)):
        c = str[i]
        for j in range(i + 1, len(str)):
            if str[j] == c:
                return False
    return True
