import math
def escape(carpark):
    result = []
    l = 1
    while 2 not in carpark[0]:
        carpark.pop(0)
    try:
        start_i = carpark[0].index(2)
    except Exception:
        return []
        
    carpark[0][start_i] = 0
    for i, level in enumerate(carpark):
        
        stairs_i = level.index(1) if 1 in level else -1
        if stairs_i == -1:
            if len(level) - start_i - 1 != 0:
                result.append(f"R{len(level) - start_i - 1}") 
            return result
        if stairs_i - start_i < 0:
            result.append(f"L{start_i - stairs_i}")
        elif stairs_i - start_i > 0:
            result.append(f"R{stairs_i - start_i}")

        if level == carpark[i + 1]:
            l += 1
        else:
            result.append(f"D{l}")
            l = 1
        start_i = stairs_i

print(escape([[1, 0, 0, 0, 2],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]))

