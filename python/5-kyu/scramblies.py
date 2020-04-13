from collections import Counter

def scramble(s1, s2):
    str1_count = Counter(s1)
    str2_count = Counter(s2)
    for k, v in str2_count.items():
        if str1_count[k] >= v:
            continue
        else:
            return False
    return True

