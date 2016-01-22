/*
 * Small benchmark to test iterative string concatenation using a variety
 * of methods. It turns out that the '+' operator is highly inefficient,
 * whereas the ostringstream, '+=' operator, and append method are all
 * practically equivalent in runtime for small input.
 *
 * With larger input (many iterations), append is fastest, then ostringstream,
 * then farther behind, '+=' operator, and of course '+' is dismal.
 *
 * Benchmark source adapted from Stack Overflow answer on 2013/9/19.
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/22
 *
 * Source: https://stackoverflow.com/questions/18892281/most-optimized-way-of-concatenation-in-strings
 */
#include <iostream>
#include <chrono>
#include <sstream>

int main()
{
    typedef std::chrono::high_resolution_clock clock;
    typedef std::chrono::duration<float, std::milli> mil;
    int num_iterations = 100000;
    std::ostringstream oss;
    const std::string start_str = "Start"; // To reset concat'd string each run
    std::string temp_str = start_str;
    oss << start_str;
    std::string content_str = "Content Data";

    // += operator
    auto t0 = clock::now();
    for (int i = 0; i < num_iterations; ++i) {
        temp_str += content_str;
    }
    auto t1 = clock::now();
    temp_str = start_str;
    std::cout << "+=: " << mil(t1 - t0).count() << "ms\n";

    // append()
    t0 = clock::now();
    for (int i = 0; i < num_iterations; ++i) {
        temp_str.append(content_str);
    }
    t1 = clock::now();
    temp_str = start_str;
    std::cout << "append: " << mil(t1 - t0).count() << "ms\n";

    // ostringstream
    t0 = clock::now();
    for (int i = 0; i < num_iterations; ++i) {
        oss << content_str;
    }
    t1 = clock::now();
    temp_str = start_str;
    std::cout << "oss: " << mil(t1 - t0).count() << "ms\n";

    // + operator
    t0 = clock::now();
    for (int i = 0; i < num_iterations; ++i) {
        temp_str = temp_str + content_str;
    }
    t1 = clock::now();
    std::cout << "+: " << mil(t1 - t0).count() << "ms\n";
}
