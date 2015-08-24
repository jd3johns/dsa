def remove_node(node):
    '''
    Given node is from somewhere in linked list, and we remove
    it by shifting the value of the next node over and deleting the next node.
    '''
    if node is None:
        return
    if node.next is None: #end node is given
        node = None
        return

    node.data = node.next.data #shift the value over
    node.next = node.next.next #remove the redundant node
    return
