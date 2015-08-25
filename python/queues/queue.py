import sys
sys.path.insert(0, '../linked_lists')

import node

class Queue(object):
    '''
    Queue data structure for generic data using linked list nodes.
    '''
    first, last = None, None

    def enqueue(self, data):
        if self.last is None:
            self.last = node.Node(data)
            self.first = self.last
        else:
            self.last.next = node.Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.first is not None:
            element = self.first.data
            self.first = self.first.next
            return element
        else:
            return None

