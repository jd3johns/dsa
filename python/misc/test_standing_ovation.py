import unittest

import standing_ovation

class TestStandingOvation(unittest.TestCase):
    ''' 
    Test cases: 
        each array value is number of audience members, 
        indexed by shyness. They never end in zero. 
    '''
    def test_standing_ovation_success(self):
        inputs = [[1,1,1,1],[0,9],[1,1,0,0,1,1],[1]]
        outputs = [0,1,2,0]
        for test, audience in enumerate(inputs):
            friends = standing_ovation.standing_ovation(audience)
            self.assertEqual(friends, outputs[test])
            print("Case #%d: %d" % (test + 1, friends))

    def test_standing_ovation_failure(self):
        input = [1,1,1,1]
        output = 1
        self.assertNotEqual(standing_ovation.standing_ovation(input), output)

if __name__ == '__main__':
    unittest.main()

