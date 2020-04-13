#My solution
def array_diff(a, b):
    for digit in b:
        a = list(filter(digit.__ne__, a))

    return a

#Other solution
# def array_diff(a, b):
#     return [x for x in a if x not in b]