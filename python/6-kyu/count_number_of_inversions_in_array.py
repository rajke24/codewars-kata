def count_inversions(array):
    return sum(1 for j in range(len(array) - 1) for i in range(j + 1, len(array)) if array[j] > array[i])