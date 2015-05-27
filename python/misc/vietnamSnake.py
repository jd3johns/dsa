#
# Problem from Programming Praxis, May 26th, 2015:
# http://programmingpraxis.com/2015/05/26/vietnam-snake/
#
# Find all the unique permutations of a set of non-repeating
# values 1-9 that represent variables A to I, and satisfy 
# the given equation:
#
#   A + (13*B)/C + D + 12*E - F - 11 + (G*H)/I - 10 = 66
# 

def findPermutations(list):
    ''' 
    Given a list of values, return a non-repeating list of all
    permutations of the values.
    '''
    # one permutation
    if len(list) == 1: 
        return [list]

    permutations = []

    for i, elem in enumerate(list):
        # swap target value into 0th place
        list[0], list[i] = list[i], list[0]
        # permutations with target value in 0th place
        subpermutations = findPermutations(list[1:len(list)])

        # collect subpermutations for target value
        for subpermutation in subpermutations:
            permutations.append([list[0]] + subpermutation)

    return permutations

def equation(list):
    ''' Vietnam Snake equation with constants pulled out'''
    return list[0] + (13*list[1])/list[2] + list[3] + 12*list[4] - list[5] + \
            list[6]*list[7]/list[8]

def solveVietnamSnake(equation, result, size):
    ''' 
    Find all possible arrangements of a list of some size that 
    satisfies a given equation that is equivalent to some number result
    '''
    solutions = []
    valueList = list(range(1, size+1))
    permutations = findPermutations(valueList)

    for permutation in permutations:
        eval = equation(permutation)
        # give some tolerance for rounding errors
        if eval < result + 0.002 and eval > result - 0.002:
            solutions.append(permutation)

    return solutions

# Test out the result
sols = solveVietnamSnake(equation, 87, 9)
print(sols)
print(len(sols))

