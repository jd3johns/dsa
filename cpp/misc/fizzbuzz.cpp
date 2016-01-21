/*
 * Simple FizzBuzz programming test. Implementation could use a larger set
 * of 'if' statements for each case but I decided to go with constructing
 * an in-memory representation of the output with a std::string, which could
 * be extended to more complex cases.
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/20
 */
#include <iostream>
#include <string>

int main()
{
    std::string msg = "";
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0) msg.append("Fizz");
        if (i % 5 == 0) msg.append("Buzz");

        if (msg.length() == 0) {
            std::cout << i;
        } else {
            std::cout << msg;
        }
        std::cout << "\n";
        msg.clear();
    }

    return 0; 
}
