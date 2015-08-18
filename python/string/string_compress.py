def string_compress(input_string):
    '''
    Compress a string of characters using simple
    repetition compression ("aa" -> "a2").
    Return original string if compression does not reduce string length
    '''

    # it's not possible to compress length 2 or shorter
    if len(input_string) <= 2:
        return input_string

    compressed_string = ""
    comparison_letter = input_string[0]
    count = 0
    for i in range(len(input_string)):
        # if recording compression pushes us over the edge, bail now
        if len(compressed_string) + 2 >= len(input_string):
            return input_string
        elif input_string[i] == comparison_letter:
            count += 1
        else:
            # string concatenation in CPython is actually O(n)
            # so this isn't a dreaded O(n^2) concatenation bottleneck
            compressed_string += comparison_letter + str(count)
            comparison_letter = input_string[i]
            count = 1

    if len(compressed_string) + 2 >= len(input_string):
        return input_string
    else:
        compressed_string += comparison_letter + str(count)

    return compressed_string

