# First solution
def longest_repetition(chars):
    most, times = 0, 0
    previous, char = '', ''
    for c in chars:
        if previous == '' or previous == c:
            times += 1
        else: 
            if times > most:
                most = times
                char = previous
                times = 1
            else:
                times = 1
        previous = c
    if times > most:
        char = previous
        most = times
    return char, most

# Second solution
def longest_repetition2(chars):
    max_char, max_count = '', 0
    previous, count = '', 0
    for c in chars:
        if c != previous:
            count, previous = 0, c
        count += 1
        if count > max_count:
            max_char, max_count = previous, count
    return max_char, max_count