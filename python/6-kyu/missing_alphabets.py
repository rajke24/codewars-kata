from collections import Counter
from string import ascii_lowercase as alphabet

def missing_alphabets1(s):
    alph = Counter('abcdefghijklmnopqrstuvwxyz')
    word = Counter(s)
    all_letters = list(''.join(([a * max(word.values()) for a in alph])))
    for x in s:
        all_letters.remove(x)
    all_letters.sort()
    return ''.join(all_letters)

def missing_alphabets2(s):
    letters = Counter(s)
    m = max(letters.values())
    return ''.join([x * (m - letters[x]) for x in alphabet])