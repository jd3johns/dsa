def binary_search(array, target):
    '''
    Complete binary search on an array for a particular value, returning
    the index of that value in the array or returning None if it is not.
    Runs recursively, partitioning the array into smaller segments each
    recursive call.
    '''
    # Base case: empty array or single value
    length = len(array)
    if length == 0:
        return None
    elif length == 1:
        if array[0] == target:
            return 0
        else:
            return None

    middle_index = length//2
    middle = array[middle_index]
    offset = 0

    # Use recursion by partitioning search space in two on each call
    if middle == target:
        index = middle_index
    elif middle < target: # Right half partition
        offset = middle_index + 1
        index = binary_search(array[middle_index+1:length], target)
    elif middle > target: # Left half partition
        offset = 0
        index = binary_search(array[0:middle_index], target)
    else:                 # Catch nonsense
        return None

    # If the recursive calls gave us an actual index, then we
    # apply the offset to the index for left/right half partitions.
    if index is not None:
        return index + offset
    else:
        return None

