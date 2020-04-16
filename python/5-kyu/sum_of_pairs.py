def sum_pairs(ints, s):
    val_set = set()
    for val in ints:
        sub = s - val
        if sub in val_set:
            return [sub, val]
        else:
            val_set.add(val)
    
# sum_pairs([1,2,3], 3)
print(sum_pairs([11, 3, 7, 5], 10))

