#
# Google Code Jam Qualification Round 2015
#
# Your friend is a prima donna in an opera, and you want
# the audience to give her a standing ovation. Each audience
# member has some level of shyness, and will only stand when some
# number of people standing before they themselves stand. 
# You can invite some number of friends that will give standing 
# ovations. What is the minimum number of friends you need 
# to invite in order to guarantee a standing ovation? (not 
# including yourself)
#

import unittest

def standingOvation(audience):
    ''' 
    Given an audience array indexed by shyness level, return the
    minimum number of friends to bring to guarantee a standing
    ovation.
    '''
    standing = 0
    friends = 0
    for shyness, n in enumerate(audience):
        newFriends = 0
        if shyness == 0 and n == 0: # initial 'stander'
            newFriends = 1
        elif shyness >= standing and n == 0: # next shyness won't stand
            newFriends = 1
        friends += newFriends
        standing += n + newFriends
    return friends

class TestStandingOvation(unittest.TestCase):
    ''' 
    Test cases: 
        each array value is number of audience members, 
        indexed by shyness. They never end in zero. 
    '''
    def test_standingOvation_success(self):
        inputs = [[1,1,1,1],[0,9],[1,1,0,0,1,1],[1]]
        outputs = [0,1,2,0]
        for test, audience in enumerate(inputs):
            friends = standingOvation(audience)
            self.assertEqual(friends, outputs[test])
            print("Case #%d: %d" % (test + 1, friends))

    def test_standingOvation_failure(self):
        input = [1,1,1,1]
        output = 1
        self.assertNotEqual(standingOvation(input), output)

if __name__ == '__main__':
    unittest.main()



