# Soluton with for loop
def anagrams1(word, words):
    return [item for item in words if sorted(word) == sorted(item)]

# Solution with filter function
def anagrams2(word, words):
    return filter(lambda k: sorted(k) == sorted(word), words)