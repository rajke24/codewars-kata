def high(x):
    return max(x.split(' '), key = lambda x: sum(ord(letter) - 96 for letter in x))