def delete_nth(order, max_e):
    result = []
    occurrences = {}

    for element in order:
        count = occurrences.setdefault(element, 0)

        if count > max_e:
            continue
        result.append(element)
        occurrences[element] += 1

    return result

def delete_nth_2(order, max_e):
    result = []
    for o in order:
        if result.count() < max_e: result.append(o)
    return result
