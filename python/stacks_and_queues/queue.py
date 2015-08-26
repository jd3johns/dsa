import sys
sys.path.insert(0, '../linked_lists')

import node

class Queue(object):
    '''
    Queue data structure for generic data using linked list nodes.
    '''
    def __init__(self):
        ''' Initialize the queue with null references to first and last '''
        self.first = None
        self.last = None

    def enqueue(self, data):
        ''' Append a new node to the back of the line '''
        if self.last is None:
            self.last = node.Node(data)
            self.first = self.last
        else:
            self.last.next = node.Node(data)
            self.last = self.last.next

    def dequeue(self):
        ''' Pull a node off of the front of the line, returning its value '''
        if self.first is not None:
            element = self.first.data
            self.first = self.first.next
            return element
        else:
            return None

