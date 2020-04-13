# My idea
def spin_words(sentence):
    words = sentence.split()
    for ind, word in enumerate(words):
        if len(word) > 4:
            words[ind] = word[::-1]

    return ' '.join(words)

# Better idea
# def spin_words(sentence):
#     return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split(' '))

