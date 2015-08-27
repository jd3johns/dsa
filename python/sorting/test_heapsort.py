import unittest

from heapsort import heapsort, heapify, sift_down

class TestHeapsort(unittest.TestCase):
    '''
    Test cases:
        Test heapify
        Test sift_down
        Test heapsort
    '''

    def test_heapify(self):
        inputs = [[3, 2, 1], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7]]
        outputs = [[3, 2, 1], [3, 2, 1], [7, 5, 6, 4, 2, 1, 3]]
        for in_array, out_array in zip(inputs, outputs):
            self.assertEqual(heapify(in_array), out_array)

    def test_sift_down(self):
        inputs = [([3, 5, 6, 4, 2, 1, 7], 0, 6)]
        outputs = [[6, 5, 7, 4, 2, 1, 3]]
        for in_args, out_array in zip(inputs, outputs):
            self.assertEqual(sift_down(in_args[0], in_args[1], in_args[2]),
                                out_array)

    def test_heapsort(self):
        inputs = [[], [1, 3, 2], [1, 4, 5, 6, 7, 9, 8, 2, 3, 0]]
        outputs = [[], [1, 2, 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
        for in_array, out_array in zip(inputs, outputs):
            self.assertEqual(heapsort(in_array), out_array)

