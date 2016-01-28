/*
 * Check if two strings are rotations of one another (ex. low, wlo).
 * (CtCI problem 1.8)
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/28
 */
#include <iostream>

/*
 * Check if two strings are rotations of one another.
 *
 * @param s1 -- first string
 * @param s2 -- second string
 * @returns bool -- true if rotation, false if not
 */
bool is_rotation(std::string s1, std::string s2)
{
    if (s1.length() != s2.length()) return false;

    // Basically 'is_substring'
    return (s1 + s1).find(s2) != std::string::npos ? true : false;
}

int main(int argc, char* argv[])
{
    if (argc < 3) {
        std::cout << "Please enter two strings" << "\n";
        return 0;
    }

    std::string s1(argv[1]), s2(argv[2]);
    std::cout << "s1: " << s1 << ", s2: " << s2 << "\n";
    std::cout << (is_rotation(s1, s2) ? "True" : "False") << "\n";
    return 0;
}
