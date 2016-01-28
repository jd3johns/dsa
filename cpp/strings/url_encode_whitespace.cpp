/*
 * URL encode the whitespace of a string with fixed length (CtCI problem 1.4).
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/28
 */
#include <iostream>
#include <cstring>

/*
 * URL encode whitespace (' ' -> '%20') of string in-place.
 * Ignore pure whitespace strings. Strings without enough trailing whitespace
 * will result in a corrupt or improperly encoded string.
 *
 * @param str -- char pointer of string to encode
 * @param len -- full length of string with trailing whitespace
 */
void url_encode_whitespace(char* str, size_t len)
{
    if (len < 3) return;

    size_t i = len - 1;
    while (str[i] == ' ') {
        if (i == 0) return;
        --i;
    }

    for (size_t j = len - 1; i < j; --i, --j) {
        if (str[i] == ' ') {
            str[j] = '0';
            str[--j] = '2';
            str[--j] = '%';
        } else {
            str[j] = str[i];
            str[i] = ' ';
        }
    }

    return;
}

int main()
{
    char buf[] = "foo b  bar      ";
    char* str = buf;
    std::cout << "Case 1: Success\n";
    std::cout << "Original string: [" << str << "]\n";
    url_encode_whitespace(str, strlen(str));
    std::cout << "Encoded string: [" << str << "]\n\n";

    char buf2[] = " foo  ";
    str = buf2;
    std::cout << "Case 2: Leading whitespace\n";
    std::cout << "Original string: [" << str << "]\n";
    url_encode_whitespace(str, strlen(str));
    std::cout << "Encoded string: [" << str << "]\n\n";

    char buf3[] = "    ";
    str = buf3;
    std::cout << "Case 3: No characters -- rejected\n";
    std::cout << "Original string: [" << str << "]\n";
    url_encode_whitespace(str, strlen(str));
    std::cout << "Encoded string: [" << str << "]\n\n";

    char buf4[] = "Mr John Smith  ";
    str = buf4;
    std::cout << "Case 4: Insufficient trailing whitespace -- failure\n";
    std::cout << "Original string: [" << str << "]\n";
    url_encode_whitespace(str, strlen(str));
    std::cout << "Encoded string: [" << str << "]\n";

    return 0;
}
