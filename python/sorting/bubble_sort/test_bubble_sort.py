import unittest

import bubble_sort

class TestBubbleSort(unittest.TestCase):
    '''
    Test bubble sort for:
        Sorted case, O(n)
        Reverse sorted case, O(n^2)
        List of length 1
        List of length 2
        Empty list
        List of strings
    '''
    def test_sorted(self):
        input = [1,2,3,4,5,6]
        output = [1,2,3,4,5,6]
        self.assertEqual(bubble_sort.bubble_sort(input), output)

    def test_reverse_sorted(self):
        input = [6,5,4,3,2,1]
        output = [1,2,3,4,5,6]
        self.assertEqual(bubble_sort.bubble_sort(input), output)

    def test_array_length_one(self):
        input = [1]
        output = [1]
        self.assertEqual(bubble_sort.bubble_sort(input), output)

    def test_array_length_two(self):
        input = [2,1]
        output = [1,2]
        self.assertEqual(bubble_sort.bubble_sort(input), output)

    def test_empty_array(self):
        input = []
        output = []
        self.assertEqual(bubble_sort.bubble_sort(input), output)

    def test_string_array(self):
        input = ['foo', 'bar', 'baz']
        output = ['bar', 'baz', 'foo']
        self.assertEqual(bubble_sort.bubble_sort(input), output)

if __name__ == '__main__':
    unittest.main()
