import unittest

import vietnam_snake

class TestVietnamSnake(unittest.TestCase):
    '''
    Test each function for success on normal input
    '''
    def test_equation_output(self):
        input = [1,2,3,4,5,6,7,8,9]
        output = 73.889
        self.assertEqual(round(vietnam_snake.equation(input), 3), output)

    def test_find_permutations_success(self):
        input = [1,2,3]
        output = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        self.assertListEqual(vietnam_snake.find_permutations(input), output)

    def test_solve_vietnam_snake(self):
        eqn = vietnam_snake.equation
        result = 87
        size = 9
        solutions = vietnam_snake.solve_vietnam_snake(eqn, result, size)

        for s in solutions:
            self.assertAlmostEqual(round(eqn(s), 3), 87)

if __name__ == '__main__':
    unittest.main()

