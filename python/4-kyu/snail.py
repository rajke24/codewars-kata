import numpy as np

def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a

arr = np.array([[1,10,3,5,6,7],[4,5,6]])
print(arr)
print(np.argmax(arr[0][::-1]))