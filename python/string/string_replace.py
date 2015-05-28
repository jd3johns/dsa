#
# Simple string replacement of a substring with a new substring
#
def string_replace(str, pattern, replace):
    return replace.join(str.split(pattern))

pattern = 'foo'
replace = 'bar'
str = 'I went to the foo to see the foos being a foo.'
print('Replace \'%s\' with \'%s\' in \'%s\'' % (pattern, replace, str))
print(string_replace(str, pattern, replace))
