def who_is_next(names, bottle_num):
    people = len(names)
    while people < bottle_num:
        bottle_num -= people
        people *= 2
    return names[int(len(names)*(bottle_num - 1) / people)]

