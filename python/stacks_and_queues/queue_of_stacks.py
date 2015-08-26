from stack import Stack

class QueueOfStacks(object):
    '''
    Queue implementation using two stacks.
    All new data is pushed onto the incoming stack.
    A dequeue pops a node off of the outgoing stack.
    If the outgoing stack is empty, the incoming stack is popped off one by one
    and pushed onto the outgoing stack such that the outgoing stack becomes a 
    reverse of the incoming stack.
    '''

    def __init__(self):
        ''' 
        Initialize the queue with two stacks -- an incoming
        and outgoing stack.
        '''
        self.incoming_stack = Stack()
        self.outgoing_stack = Stack()

    def enqueue(self, item):
        ''' Push the new data onto the first, incoming, stack '''
        if item is not None:
            self.incoming_stack.push(item)

    def dequeue(self):
        ''' 
        Pop the first in line off the second, outgoing, stack. If empty,
        reverse the incoming stack onto the outgoing stack then pop one off.
        '''
        if not self.outgoing_stack.is_empty():
            return self.outgoing_stack.pop()
        elif not self.incoming_stack.is_empty():
            while not self.incoming_stack.is_empty():
                self.outgoing_stack.push(self.incoming_stack.pop())
            return self.outgoing_stack.pop()
        else:
            return None

