from collections import Counter

def first_non_repeating_letter(string):
    count = Counter(string.lower())
    for c in string:
        if count[c.lower()] == 1:
            return c 
    return ''