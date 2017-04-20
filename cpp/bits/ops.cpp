#include <iostream>
#include <stdexcept>

static size_t MAX_BITS = 8 * sizeof(unsigned long long);

// Test whether bit is set. Throws exception if bit
// is outside the range of the integer type (i.e. higher
// than 64th bit).
bool test(const unsigned long long num, const size_t idx)
{
    if (idx > MAX_BITS - 1)
        throw std::out_of_range("index too high");

    return (num & (1ull << idx)) > 0;
}

// Clear all bits.
void clear(unsigned long long *num)
{
    (*num) &= 0ull;
}

// Flip a particular bit on or off. Will
// throw std::out_of_range if index exceeds
// size of integer type.
void set(unsigned long long *num, const size_t idx, const bool val = true)
{
    if (idx > MAX_BITS - 1)
        throw std::out_of_range("index too high");

    if (val)
    {
        (*num) |= (1ull << idx);
    }
    else
    {
        (*num) &= ~(1ull << idx);
    }
}

int main()
{
    unsigned long long a = 0b0100;
    std::cout << "a = " << a << std::endl;
    if (test(a, 2))
    {
        std::cout << "third bit is set in a\n";
    }

    a = 0b0010;
    std::cout << "a = " << a << std::endl;
    if (!test(a, 2))
    {
        std::cout << "third bit is not set in a\n";
    }

    std::cout << "clear a\n";
    clear(&a);
    std::cout << "a = " << a << std::endl;


    std::cout << "set 9th bit of a\n";
    set(&a, 8);
    std::cout << "a = " << a << std::endl;

    std::cout << "set 1st bit of a\n";
    set(&a, 0);
    std::cout << "a = " << a << std::endl;

    std::cout << "turn off 1st bit of a\n";
    set(&a, 0, false);
    std::cout << "a = " << a << std::endl;

    try
    {
        std::cout << "set 65th bit of a\n";
        set(&a, 64);
        std::cout << "a = " << a << std::endl;
    }
    catch (std::out_of_range& e)
    {
        std::cout << "I'm sorry Dave, I'm afraid I can't let you do that... "
                  << e.what() << std::endl;
    }
    catch (std::exception& e)
    {
        std::cout << "some exception: " << e.what() << std::endl;
    }
}
