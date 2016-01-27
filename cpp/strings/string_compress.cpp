/*
 * Simple string compression algorithm (CtCI problem 1.5)
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/27
 */
#include <iostream>

/*
 * Compress a string that contains no numbers by placing the count of
 * repeated characters after that character (ex. aaa -> a3).
 *
 * @param str -- input string to compress
 * @returns   -- if compression results in larger or equal string, input
 *               if compression results in smaller string, compressed string
 */
std::string compress(std::string str)
{
    size_t slen = str.length();
    if (slen <= 2) return str;

    std::string compress_str;
    compress_str += str[0];
    char current = str[0];
    int count = 1;
    for (size_t i = 1; i < slen; ++i) {
        if (current == str[i]) {
            count++;
            continue;
        } else {
            compress_str += std::to_string(count);
            compress_str += str[i];
            current = str[i];
            count = 1;
        }

        if (compress_str.length() >= slen) {
            return str;
        }
    }

    compress_str += std::to_string(count);
    return compress_str;
}

int main(int argc, char* argv[])
{
    std::string str = "aaabb";
    std::cout << "Original string: " << str << "\n";
    std::cout << "Compressed string: " << compress(str) << "\n";

    str = "ab";
    std::cout << "Original string: " << str << "\n";
    std::cout << "Compressed string: " << compress(str) << "\n";

    str = "abc";
    std::cout << "Original string: " << str << "\n";
    std::cout << "Compressed string: " << compress(str) << "\n";

    str = "aaabbbcddeeeeee";
    std::cout << "Original string: " << str << "\n";
    std::cout << "Compressed string: " << compress(str) << "\n";

    return 0;
}
