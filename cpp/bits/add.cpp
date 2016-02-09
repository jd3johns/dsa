/*
 * Add two numbers without using the addition operator or any other arithmetic
 * operators, for that matter. (CtCI problem 18.1)
 *
 * Author: Jonathan Johnston
 * Date: 2016/2/8
 */
#include <iostream>
#include <stdexcept>

/*
 * CtCI book solution
 */
int add(int a, int b)
{
    if (b == 0) return a;
    int sum = a ^ b;
    int carry = (a & b) << 1;
    return add(sum, carry);
}

/*
 * Add two 16-bit unsigned integers without recursion or any arithmetic
 * operators, throwing if overflow occurs.
 *
 * @param a -- first number to add
 * @param b -- second number to add
 * @returns uint16 -- sum of two numbers
 * @throws exception -- if overflow occurs in addition
 */
uint16_t uadd(uint16_t a, uint16_t b)
{
    const int num_bits = 16;
    uint16_t res = 0, mask = 1;
    bool overflow = false;
    bool a_set = false, b_set = false;

    // consider each bit
    for (int i = 0; i < num_bits; ++i) {
        mask = (i == 0) ? mask : mask << 1; // consider next bit
        a_set = (a & mask) != 0;
        b_set = (b & mask) != 0;

        if (overflow) {
            res |= mask; // set the bit
            overflow = false; // done overflow
        }

        if (a_set && b_set) { // both set
            overflow = true; // carry over
        } else if (a_set || b_set) { // one set
            if ((res & mask) != 0) {
                res ^= mask; // turn off bit
                overflow = true; // carry over
            } else {
                res |= mask; // not set so turn on bit
            }
        }
    }

    if (overflow) {
        //throw std::overflow_error::overflow_error("overflow in addition");
        throw std::overflow_error("overflow in addition of "
                + std::to_string(a) + " and " + std::to_string(b));
    }

    return res;
}

int main() {
    // Test own solution
    uint16_t a, b;

    a = 1, b = 1;
    std::cout << "Test 1: ";
    std::cout << a << " + " << b << " = " << uadd(a,b) << "\n";

    try {
        a = 65534, b = 2; // overflow results in throw
        std::cout << "Test 2: ";
        std::cout << a << " + " << b << " = " << uadd(a,b) << "\n";
    } catch (std::exception& e) {
        std::cout << e.what() << "\n";
    }

    a = 100, b = 100;
    std::cout << "Test 3: ";
    std::cout << a << " + " << b << " = " << uadd(a,b) << "\n";

    a = 9999, b = 10000;
    std::cout << "Test 4: ";
    std::cout << a << " + " << b << " = " << uadd(a,b) << "\n";

    // Test book solution
    int c, d; // usually 32 bit

    c = 2147483646, d = 1; // signed solution; as expected
    std::cout << "Test 5 (soln): ";
    std::cout << c << " + " << d << " = " << add(c, d) << "\n";

    c = 2147483646, d = 2; // signed solution; overflow to signed bit
    std::cout << "Test 6 (soln): ";
    std::cout << c << " + " << d << " = " << add(c, d) << "\n";
}
