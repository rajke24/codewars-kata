def add(num1, num2):
    max_l = max([num1,num2])
    num1, num2 = str(num1).zfill(max_l), str(num2).zfill(max_l)
    result = ''
    for x, y in zip(num1, num2):
        result += str(int(x) + int(y))

    return int(result)        