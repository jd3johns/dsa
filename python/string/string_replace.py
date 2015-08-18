def string_replace(string, pattern, replace):
    ''' Simple string replacement of a substring with a new substring '''
    return replace.join(string.split(pattern))

pattern = 'foo'
replace = 'bar'
string = 'I went to the foo to see the foos being a foo.'
print('Replace \'%s\' with \'%s\' in \'%s\'' % (pattern, replace, string))
print(string_replace(string, pattern, replace))
