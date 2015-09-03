'''
Top-down mergesort algorithm from Sedgewick's Algorithms in Java
Parts 1-4.
'''

def merge(array, left, middle, right):
    '''
    Merge two sorted subsections of a list back into the array
    as an abstract in-place merge. Stable merge.
    '''
    # Copy sorted lists into auxiliary memory
    left_aux = array[left:middle+1]
    right_aux = array[middle+1:right+1]

    # Set indices to start of lists
    left_idx, right_idx = 0, 0

    # Merge lists into original array
    for i in range(left, right + 1):
        if left_idx >= len(left_aux):
            array[i] = right_aux[right_idx]
            right_idx += 1
        elif right_idx >= len(right_aux):
            array[i] = left_aux[left_idx]
            left_idx += 1
        elif left_aux[left_idx] <= right_aux[right_idx]:
            array[i] = left_aux[left_idx]
            left_idx += 1
        else:
            array[i] = right_aux[right_idx]
            right_idx += 1

def mergesort(array, left, right):
    '''
    Sort a list using the standard top-down mergesort algorithm.
    '''
    if left >= right:
        return
    
    middle = (left + right)//2
    mergesort(array, left, middle)
    mergesort(array, middle + 1, right)
    merge(array, left, middle, right)

