def unique_in_order(iterable):
    prev = ''
    result = []
    for letter in iterable:
        if letter != prev:
            result.append(letter)
        prev = letter

    return result
    