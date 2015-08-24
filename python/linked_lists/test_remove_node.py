import unittest

import node
import remove_node

class TestRemoveNode(unittest.TestCase):
    '''
    Test cases:
        Empty: return
        End node: a -> b -> (c)
        Middle node: a -> (b) -> c
        Head node: (a) -> b -> c
    '''

    def test_empty(self):
        in_node = None
        remove_node.remove_node(in_node)
        self.assertIsNone(in_node)

    def test_end_node(self):
        head = node.Node('a')
        head.next = node.Node('b')
        head.next.next = node.Node('c')
        in_node = head.next.next
        outputs = ['a','b']

        remove_node.remove_node(in_node)
        n = head
        for value in outputs:
            self.assertEqual(n.data, value)
            n = n.next

    def test_middle_node(self):
        head = node.Node('a')
        head.next = node.Node('b')
        head.next.next = node.Node('c')
        in_node = head.next
        outputs = ['a','c']
                                            
        remove_node.remove_node(in_node)
        n = head
        for value in outputs:
            self.assertEqual(n.data, value)
            n = n.next

    def test_head_node(self):
        head = node.Node('a')
        head.next = node.Node('b')
        head.next.next = node.Node('c')
        in_node = head
        outputs = ['b','c']
                                            
        remove_node.remove_node(in_node)
        n = head
        for value in outputs:
            self.assertEqual(n.data, value)
            n = n.next
