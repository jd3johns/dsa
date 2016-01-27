/*
 * Author: Jonathan Johnston
 * Date: 2016/1/20
 */
#include <inttypes.h>
#include <iostream>

int main()
{
    unsigned long n, m, a;
    scanf("%lu %lu %lu", &n, &m, &a);
    if (a < 1 or n < 1 or m < 1)
    {
        printf("%d", 0);
        return 0;
    }
    uint64_t x = (n % a) == 0 ? n/a : (n/a + 1);
    uint64_t y = (m % a) == 0 ? m/a : (m/a + 1);
    std::cout << (x * y);
    return 0;
}
