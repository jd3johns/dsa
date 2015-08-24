def remove_node(node):
    '''
    Given node is from somewhere in linked list, and we remove
    it by shifting the values of the nodes and deleting the last node.
    '''
    if node is None:
        return

    while node.next is not None:
        node.data = node.next.data #shift the values up
        node = node.next

    node = None #delete final node
    return
