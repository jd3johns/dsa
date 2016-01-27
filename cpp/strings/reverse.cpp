/*
 * C string reverse (CtCI problem 1.2)
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/27
 */
#include <iostream>
#include <cstring>

/*
 * Reverse a null-terminated C-string.
 *
 * @param str -- pointer to string to reverse
 */
void reverse(char* str)
{
    size_t slen = strlen(str);
    if (slen <= 2) return;

    size_t size = slen + sizeof(char); //add one more char for null term.
    char buf[size];
    strncpy(buf, str, size); //strncpy takes care of null termination
    for (size_t i = 0; i < slen; i++) {
        str[i] = buf[(slen - 1) - i]; //copy from end, past null
    }
}

int main(int argc, char* argv[])
{
    if (argc < 2) {
        std::cout << "Enter a sequence of characters" << "\n";
        return 0;
    }

    char* input = argv[1];
    std::cout << "Original string: " << input << "\n";
    reverse(input);
    std::cout << "After reverse: " << input << "\n";

    return 0;
}
