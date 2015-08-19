import unittest

import is_permutation

class TestIsPermutation(unittest.TestCase):
    '''
    Test cases:
        Empty: ""
        Varying lengths: ex. "water", "waterw"
        Not permutation: ex. "water", "terwz"
        Case insensitivity: ex. "water", "wAtEr"
        True permutation: ex. "water", "aetrw"
    '''

    def test_empty(self):
        inputs = [("", "")]
        for str1, str2 in inputs:
            self.assertFalse(is_permutation.is_permutation(str1, str2))

    def test_length_mismatch(self):
        inputs = [("water", "aterwa"), ("Mississippi", "issississippiM")]
        for str1, str2 in inputs:
            self.assertFalse(is_permutation.is_permutation(str1, str2))

    def test_not_permutation(self):
        inputs = [("water", "terwz"), ("abcde", "eabca")]
        for str1, str2 in inputs:
            self.assertFalse(is_permutation.is_permutation(str1, str2))

    def test_case_insensitivity(self):
        inputs = [("abc", "ABC")]
        for str1, str2 in inputs:
            self.assertTrue(is_permutation.is_permutation(str1, str2))

    def test_true_permutation(self):
        inputs = [("waterbottle", "abeetrwoltt"), ("abcdefg", "defgabc")]
        for str1, str2 in inputs:
            self.assertTrue(is_permutation.is_permutation(str1, str2))

if __name__ == '__main__':
    unittest.main()
