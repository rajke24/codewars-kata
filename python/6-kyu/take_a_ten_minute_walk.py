from collections import Counter

def is_valid_walk(walk):
    count = Counter(walk)
    return count['n'] == count['s'] and count['e'] == count['w'] and len(walk) == 10

# other solution
# def is_valid_walk(walk):
#     return len(walk) == 10 and walk.count('n') ==  walk.count('s') and  walk.count('e') ==  walk.count('w') 