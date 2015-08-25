import sys
sys.path.insert(0, '../linked_lists')

import node

class Stack(object):
    '''
    Stack data structure for generic data using linked list nodes.
    '''
    top = None

    def push(self, data):
        new_top = node.Node(data)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        if self.top is not None:
            element = self.top.data
            self.top = self.top.next
            return element
        else:
            return None

    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            return None
