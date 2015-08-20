class Node(object):
    '''
    Singly-linked list class for generic data
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def append_to_tail(self, data):
        ''' find the end of the list and append a node '''
        n = self
        while n.next is not None:
            n = n.next
        n.next = Node(data)

