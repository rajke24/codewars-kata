def tower_builder(n_floors):
    if n_floors == 1: return ['*']
    last_floor_width = (n_floors - 1) * 2 + 1
    return [((last_floor_width - (i + 1) * 2 + 1) / 2) * ' ' + (1 + i * 2) * '*' + ((last_floor_width - (i + 1) * 2 + 1)/2) * ' ' for i in range( n_floors)]

def tower_builder2(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]