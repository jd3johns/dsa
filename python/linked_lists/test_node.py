import unittest

import node

class TestNode(unittest.TestCase):
    '''
    Test cases:
        Constructing a node: ex. n = Node(8)
    '''

    def test_successful_construction(self):
        inputs = [-1, 0, 5.0, 'foo', 'bar', True]
        for data in inputs:
            linked_list = node.Node(data)
            self.assertEqual(linked_list.data, data)
            self.assertIsNone(linked_list.next)

    #def test_append_to_tail(self):
    #    inputs = ["", ""]

if __name__ == "__main__":
    unittest.main()
