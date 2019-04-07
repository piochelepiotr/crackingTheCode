def is_one_remove_away(word1: str, word2: str) -> bool:
    """
    Returns true if by removing one letter from the long word,
    we can get the short word
    """
    if len(word1) == len(word2) + 1:
        short_word = word2
        long_word = word1
    elif len(word1) + 1 == len(word2):
        short_word = word1
        long_word = word2
    else:
        return False

    for i in range(len(long_word)):
        if short_word == long_word[0:i] + long_word[i + 1 :]:
            return True
    return False


def is_one_replace_away(word1: str, word2: str) -> bool:
    """
    Returns True if by replacing one letter in word1,
    we can get word2
    """
    if len(word1) != len(word2):
        return False
    already_one_character_diff = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if already_one_character_diff:
                return False
            already_one_character_diff = True
    return True


def is_one_operation_away(word1: str, word2: str) -> bool:
    return is_one_remove_away(word1, word2) or is_one_replace_away(word1, word2)
