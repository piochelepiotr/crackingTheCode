from collections import Counter

def sort_anagram(l):
    def letter_count(w):
        counts = Counter(w)
        return [counts[chr(c)] for c in range(ord('a'), ord('z')+1)]
    l.sort(key=letter_count)
    return l
