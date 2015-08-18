import unittest

import is_rotation

class TestIsRotation(unittest.TestCase):
    '''
    Test cases:
        Empty: ""
        Varying lengths: ex. "water", "aterwa"
        Not rotation: ex. "water", "terwz"
        True rotation: ex. "water", "terwa"
    '''

    def test_empty(self):
        inputs = [("", "")]
        for str1, str2 in inputs:
            self.assertFalse(is_rotation.is_rotation(str1, str2))

    def test_length_mismatch(self):
        inputs = [("water", "aterwa"), ("Mississippi", "issississippiM")]
        for str1, str2 in inputs:
            self.assertFalse(is_rotation.is_rotation(str1, str2))

    def test_not_rotation(self):
        inputs = [("water", "terwz"), ("abcde", "eabca")]
        for str1, str2 in inputs:
            self.assertFalse(is_rotation.is_rotation(str1, str2))

    def test_true_rotation(self):
        inputs = [("waterbottle", "terbottlewa"), ("abcdefg", "defgabc")]
        for str1, str2 in inputs:
            self.assertTrue(is_rotation.is_rotation(str1, str2))

if __name__ == '__main__':
    unittest.main()
