# First idea
def max_sequence(arr):
    if not arr:
        return 0
    elif min(arr) >= 0:
        return sum(arr)
    max_sum = 0
    max_ending = 0
    for x in arr:
        max_ending += x
        if max_ending > max_sum:
            max_sum = max_ending
        elif max_ending < 0:
            max_ending = 0
    return max_sum

# Improved code
def max_sequence2(arr):
    max_sum, max_ending = 0, 0
    for x in arr:
        max_ending += x
        if max_ending < 0: max_ending = 0
        if max_ending > max_sum: max_sum = max_ending
    return max_sum        

