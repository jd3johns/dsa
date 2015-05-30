def bubble_sort(array):
    ''' Bubble sort an array of inequality-comparable type '''
    length = len(array)
    if length <= 1:
        return array

    for i in range(length):
        swap = False
        for j in range(1, length):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                swap = True
        if not swap:
            break # no swaps means array is sorted

    return array
