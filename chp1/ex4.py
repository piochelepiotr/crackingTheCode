def is_palindrome_permutation(word):
    """
    Returns if a word is a permutation of a palindrome
    This is the case only if it has maximum one letter
    with an odd count
    """
    # not case or space sensitive
    word = word.lower().replace(" ", "")
    letter_count = {}
    for c in word:
        try:
            letter_count[c] += 1
        except KeyError:
            letter_count[c] = 1
    odd_letter_count = False
    for c in letter_count:
        if letter_count[c] % 2 == 1:
            if odd_letter_count:
                return False
            odd_letter_count = True
    return True
