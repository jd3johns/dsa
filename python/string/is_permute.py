def is_permutation(str1, str2):
    '''
    Determine whether one string is a permutation of another using
    a dictionary to compare the counts of characters.
    Runs in O(n) time and O(1) space (due to finite character set).
    '''
    if len(str1) != len(str2) or len(str1) < 1:
        return False

    char_count = dict()
    for char in str1.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2.lower():
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    for count in char_count.values():
        if count != 0:
            return False

    return True


