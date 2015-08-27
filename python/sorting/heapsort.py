import sys

def heapsort(array):
    ''' 
    Execute heapsort on an array by creating a max heap structure
    of the array and swapping the max value onto the end of the heap.
    '''
    # Turn the array into a heap
    heapify(array)

    end = len(array) - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        sift_down(array, 0, end)
    
    return array


def heapify(array):
    ''' Turn an array into a heap '''
    # Start at the first parent node
    start = (len(array) - 2)//2
    end = len(array) - 1

    # Go through each parent and percolate it down to
    # create the recursive max heap property
    while start >= 0:
        sift_down(array, start, end)
        start -= 1

    return array


def sift_down(array, start, end):
    ''' Percolate a parent down a heap to maintain the max heap property '''
    root = start

    # Continue as long as there are children
    while 2*root + 1 <= end:
        child = 2*root + 1
        swap = root

        if array[swap] < array[child]:
            swap = child
        # Does right child exist? Check it against current candidate
        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1

        if swap == root:
            return
        else:
            array[swap], array[root] = array[root], array[swap]
            root = swap

    return array

