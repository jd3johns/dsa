import sys
sys.path.insert(0, '../linked_lists')

import node

class Stack(object):
    '''
    Stack data structure for generic data using linked list nodes.
    '''
    def __init__(self):
        ''' Initialize the stack as being a null pointer to the top '''
        self.top = None

    def push(self, data):
        ''' Push a node on top of the stack '''
        new_top = node.Node(data)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        ''' Pop the top node off of the stack and return its value '''
        if self.top is not None:
            element = self.top.data
            self.top = self.top.next
            return element
        else:
            return None

    def peek(self):
        ''' Return the value of the top node of the stack '''
        if self.top is not None:
            return self.top.data
        else:
            return None
