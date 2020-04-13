from collections import Counter

def getCount(inputStr):
    vowels = ['a', 'e', 'o', 'i', 'u']
    counter = Counter(inputStr)
    return sum(counter[c] for c in vowels)
