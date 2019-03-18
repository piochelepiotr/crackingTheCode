def get_compressed_word(word: str) -> str:
    current_character = None
    i = 0
    compressed_char_list = []
    while i < len(word):
        current_character = word[i]
        count = 0
        while i < len(word) and word[i] == current_character:
            i += 1
            count += 1
        compressed_char_list.append((current_character, count))
    compressed_word = ""
    for c, count in compressed_char_list:
        compressed_word += str(count) + c
    if len(compressed_word) >= len(word):
        return word
    return compressed_word


assert get_compressed_word("aaaabbccc") == "4a2b3c"
