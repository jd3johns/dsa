import unittest

import node
import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    '''
    Test cases:
        Empty: no node
        One node: ex. 'a'
        No duplicates: ex. 'a' -> 'b' -> 'c'
        Duplicates: ex. 'a' -> 'a' -> 'a'
    '''

    def test_empty(self):
        inputs = [None]
        for head in inputs:
            self.assertEqual(remove_duplicates.remove_duplicates(head), head)

    def test_one_node(self):
        inputs = ['a', 'b', 'c']
        for head_value in inputs:
            head = node.Node(head_value)
            self.assertEqual(remove_duplicates.remove_duplicates(head), head)

    def test_no_duplicates(self):
        inputs = [('a', 'b', 'c'), (1, 2, 3)]
        outputs = [('a', 'b', 'c'), (1, 2, 3)]
        for in_list, out_list in zip(inputs, outputs):
            in_head = node.Node(in_list[0])
            in_n = in_head
            for value in in_list:
                in_n.next = node.Node(value)
                in_n = in_n.next

            head = remove_duplicates.remove_duplicates(in_head)
            n = head
            for value in out_list:
                self.assertEqual(n.data, value)
                n = n.next

    def test_duplicates(self):
        inputs = [('a', 'a', 'a', 'a'), (1, 2, 2, 3, 2, 1)]
        outputs = [('a'), (1, 2, 3)]
        for in_list, out_list in zip(inputs, outputs):
            in_head = node.Node(in_list[0])
            in_n = in_head
            for value in in_list:
                in_n.next = node.Node(value)
                in_n = in_n.next

            head = remove_duplicates.remove_duplicates(in_head)
            n = head
            for value in out_list:
                self.assertEqual(n.data, value)
                n = n.next
