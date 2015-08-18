def is_rotation(str1, str2):
    ''' Check if one string is a rotation of the other, ex. 'abc', 'bca'. '''
    if len(str1) == len(str2) and len(str1) > 0:
        # is_substring method can be replaced with Python 'in' membership check
        return str1 in str2 + str2
    else:
        return False

