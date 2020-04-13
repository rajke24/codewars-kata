def move_zeros(array):
    length = len(array) 
    i = 0
    while(i < length):
        x = array[i]
        if x == 0  and type(x) != bool:
            array.pop(i)
            length -= 1
            if i > 0:
                i -= 1
            array.append(0)
            continue
        i += 1

    return array
    
# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))


print(move_zeros([False,1,0.0,1,1,0,0,2,0,'x']))
print()