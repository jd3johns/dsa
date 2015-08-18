import unittest

import string_compress

class TestStringCompress(unittest.TestCase):
    '''
    Test cases:
        Empty: ""
        Incompressible of varying lengths: ex. "aa"
        Compressible of varying lengths: ex. "aaabb"
    '''

    def test_empty(self):
        in_str = ""
        out_str = ""
        self.assertEqual(string_compress.string_compress(in_str), out_str)

    def test_incompressible(self):
        inputs = ["aa", "aab", "aabb", "abcd"]
        outputs = ["aa", "aab", "aabb", "abcd"]
        for in_str, out_str in zip(inputs, outputs):
            self.assertEqual(string_compress.string_compress(in_str), out_str)

    def test_compressible(self):
        inputs = ["aaabb", "aaabbcc", "abbcddddd"]
        outputs = ["a3b2", "a3b2c2", "a1b2c1d5"]
        for in_str, out_str in zip(inputs, outputs):
            self.assertEqual(string_compress.string_compress(in_str), out_str)

if __name__ == '__main__':
    unittest.main()
