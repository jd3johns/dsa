/*
 * C string reverse (CtCI problem 1.2)
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/27
 */
#include <iostream>
#include <cstring>
#include <chrono>

using clk = std::chrono::high_resolution_clock;
using mil = std::chrono::duration<float, std::milli>;

/*
 * Reverse a null-terminated C-string in place.
 *
 * @param str -- pointer to string to reverse
 */
void reverse(char* str)
{
    size_t slen = strlen(str);
    if (slen < 2) return;
    char tmp;

    // swap front and back, stopping in middle
    for (size_t i = 0; i < (slen / 2); ++i) {
        tmp = str[i];
        str[i] = str[(slen - 1) - i];
        str[(slen - 1) - i] = tmp;
    }
}

/*
 * Reverse a null-terminated C-string with a memory buffer.
 */
void reverse_with_buffer(char* str)
{
    size_t slen = strlen(str);
    if (slen <= 2) return;

    size_t size = slen + sizeof(char); // add one more char for null term.
    char buf[size];
    strncpy(buf, str, size); // strncpy takes care of null termination
    for (size_t i = 0; i < slen; i++) {
        str[i] = buf[(slen - 1) - i]; // copy from end, past null
    }
}

int main(int argc, char* argv[])
{
    if (argc < 2) {
        std::cout << "Enter a sequence of characters" << "\n";
        return 0;
    }

    // Time input using both in-place and memory buffer algos
    // in-place
    char* input = argv[1];
    std::cout << "Original string: " << input << "\n";
    auto start = clk::now();
    reverse(input);
    auto end = clk::now();

    std::cout << "After reverse: " << input << "\n";
    std::cout << "in-place runtime: " << mil(end - start).count() << "ms\n\n";
    reverse(input); // reset

    // memory buffer
    // ~50% slower than in-place algorithm
    std::cout << "Reset original string: " << input << "\n";
    start = clk::now();
    reverse_with_buffer(input);
    end = clk::now();

    std::cout << "After reverse: " << input << "\n";
    std::cout << "memory buffer runtime: " << mil(end - start).count() << "ms\n";

    return 0;
}
