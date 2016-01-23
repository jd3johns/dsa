/*
 * Print out the bit sizes of fundamental C++ data types for
 * the compiler and machine used to compile and run the source,
 * respectively.
 *
 * Note: For more complex understanding of machine- and compiler-specific
 *       limits and properties of fundamental data types, the <limits> lib
 *       can be used (in addition to programmatic use of data type limits).
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/19
 */
#include <iostream>

using namespace std;

int main()
{
    cout << "Bit size of C++ data types for your compiler and system:\n";
    cout << "Character types:\n";
    cout << "char: " << 8*sizeof(char) << "\n";
    cout << "char16_t: " << 8*sizeof(char16_t) << "\n";
    cout << "char32_t: " << 8*sizeof(char32_t) << "\n";
    cout << "wchar_t: " << 8*sizeof(wchar_t) << "\n";
    cout << "\n";

    cout << "Signed integer types:\n";
    cout << "signed char: " << 8*sizeof(signed char) << "\n";
    cout << "short: " << 8*sizeof(short) << "\n";
    cout << "int: " << 8*sizeof(int) << "\n";
    cout << "long: " << 8*sizeof(long) << "\n";
    cout << "long long: " << 8*sizeof(long long) << "\n";
    cout << "\n";

    cout << "Floating-point types:\n";
    cout << "float: " << 8*sizeof(float) << "\n";
    cout << "double: " << 8*sizeof(double) << "\n";
    cout << "long double: " << 8*sizeof(long double) << "\n";
    cout << "\n";

    cout << "Other types\n";
    cout << "bool: " << 8*sizeof(bool) << "\n";
    //cout << "void: " << 8*sizeof(void) << "\n";
    cout << "decltype(nullptr): " << 8*sizeof(decltype(nullptr));

    return 0;
}
