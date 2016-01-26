/*
 * Simple program to echo the arguments entered.
 *
 * Author: Jonathan Johnston
 * Date: 2016/1/26
 */
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    cout << "argc: " << argc << "\n";
    for (int i = 0; i < argc; ++i) {
        cout << "argv[" << i << "]: " << argv[i] << "\n";
    }
}
