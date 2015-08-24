def remove_duplicates(head):
    '''
    Remove duplicate values in a linked list, keeping the first
    occurrence of the value. Runs in O(n) time and space using a dict.
    '''
    if head is None or head.next is None:
        return head

    duplicate_dict = dict()
    node = head
    duplicate_dict[node.data] = 1

    while node.next is not None:
        if node.next.data in duplicate_dict:
            node.next = node.next.next
        else:
            duplicate_dict[node.next.data] = 1
            node = node.next

    return head
