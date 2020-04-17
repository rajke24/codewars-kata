def who_eats_who(zoo):
    eats = {"antelope"    : ["grass"],
            "big-fish"    : ["little-fish"],
            "bug"         : ["leaves"],
            "bear"        : ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
            "chicken"     : ["bug"],
            "cow"         : ["grass"],
            "fox"         : ["chicken", "sheep"],
            "giraffe"     : ["leaves"],
            "lion"        : ["antelope", "cow"],
            "panda"       : ["leaves"],
            "sheep"       : ["grass"],
            "grass"       : [],
            "leaves"      : [],
            "little-fish" : []}
    
    output, input_lst, i = [zoo], zoo.split(','), 0
   
    while i < len(input_lst):
        cur_el = input_lst[i]
        item_left = input_lst[i - 1]
    
        if i > 0 and item_left in eats.get(cur_el, []):
            output.append(f"{cur_el} eats {item_left}")
            input_lst.pop(i - 1)
            i = 0
        elif i < len(input_lst) - 1 and input_lst[i+1] in eats.get(cur_el, []):
            output.append(f"{cur_el} eats {input_lst[i+1]}")
            input_lst.pop(i + 1)
            i = 0
        else:
            i += 1
    output.append(','.join(input_lst))
    return output

print(who_eats_who("fox,bug,chicken,grass,sheep"))