def is_permutation(str1, str2):
    '''
    Check if one string is a permutation of the other by using sorting.
    We normalize to case insensitivity.
    '''
    if len(str1) == len(str2) and len(str1) > 0:
        return sorted(str1.lower()) == sorted(str2.lower())
    else:
        return False


