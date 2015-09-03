import unittest

from mergesort import mergesort

class TestMergesort(unittest.TestCase):
    '''
    Test cases:
        Standard array
    '''

    def test_normal_input(self):
        array = [7, 5, 6, 8, 9, 0, 3, 4, 2, 2, 1]
        output = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

        mergesort(array, 0, len(array) - 1)
        self.assertEqual(array, output)

