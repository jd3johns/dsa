import unittest

from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    '''
    Test cases:
        Empty array: x = []
        Single element: x = [1]
        Two elements: x = [1, 2]
        Three elements: x = [1, 2, 4]
        N elements: x = [1, 4, 6, 7, 9, ...]
    '''

    def test_empty(self):
        self.assertIsNone(binary_search([], 1))

    def test_single_element(self):
        # Value not in set
        self.assertIsNone(binary_search([1], 2))
        # Value in set
        self.assertEqual(binary_search([1], 1), 0)

    def test_two_elements(self):
        # Value not in set
        self.assertIsNone(binary_search([1, 2], 0))
        # Value in set
        self.assertEqual(binary_search([1, 2], 2), 1)

    def test_three_elements(self):
        # Value not in set
        self.assertIsNone(binary_search([1, 2, 3], 4))
        # Value in set
        self.assertEqual(binary_search([1, 2, 3], 2), 1)

    def test_n_elements(self):
        in_array = [1, 2, 5, 6, 8, 9, 13, 17, 29]

        # Value not in set
        # Below range
        self.assertIsNone(binary_search(in_array, -4))
        # In range
        self.assertIsNone(binary_search(in_array, 14))
        # Above range
        self.assertIsNone(binary_search(in_array, 51))

        # Value in set
        for i, elem in enumerate(in_array):
            self.assertEqual(binary_search(in_array, elem), i)


