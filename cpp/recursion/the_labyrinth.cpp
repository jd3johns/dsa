/*
 * The Labyrinth (CodeForces Problem 616C)
 *
 * Input of 0 <= n, m <= 1000 as rows and columns,
 * then a matrix consisting of '*' as blocks and '.' as empty cells.
 *
 * For each block ('*'), imagine it were empty, and measure the length of
 * the connected component (number of consecutive adjacent empty spaces)
 * which contains that block. Output the matrix, but replace the blocks
 * with the integer length of the connected component (mod 10).
 *
 * Author: Jonathan Johnston
 * Date: 2016/2/4
 */
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <chrono>

using namespace std;
using timeclock = chrono::high_resolution_clock;
using mil = chrono::duration<float, milli>;

/*
 * Perform depth-first search to find size of connected component containing
 * element (i,j).
 */
int dfs(const vector<char>& mat, const int rows, const int cols,
        int i, int j, vector<bool>& visited)
{
    if (mat[i*cols + j] != '.') return 0;

    int size = 1;
    visited[i*cols + j] = true;

    if (i + 1 < rows && !visited[(i + 1)*cols + j]) {
        size += dfs(mat, rows, cols, i + 1, j, visited);
    }
    if (j + 1 < cols && !visited[i*cols + (j + 1)]) {
        size += dfs(mat, rows, cols, i, j + 1, visited);
    }
    if (i - 1 >= 0 && !visited[(i - 1)*cols + j]) {
        size += dfs(mat, rows, cols, i - 1, j, visited);
    }
    if (j - 1 >= 0 && !visited[i*cols + (j - 1)]) {
        size += dfs(mat, rows, cols, i, j - 1, visited);
    }

    return size;
}

int main()
{
    auto start = timeclock::now();
    int n, m; // rows, cols
    char row[1001]; // big enough for input size
    scanf("%d %d", &n, &m);
    vector<char> mat(n*m);

    // Scan for input matrix
    for (int i = 0; i < n; ++i) {
        scanf("%s", row);
        for (int j = 0; j < m; ++j) {
            mat[i*m + j] = row[j];
        }
    }
    auto end = timeclock::now();
    cout << "input time: " << mil(end - start).count() << "\n";

    start = timeclock::now();
    // Perform depth-first search and assign connected component size to elem
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i*m + j] == '*') {
                mat[i*m + j] = '.';
                vector<bool> visited(n*m); // initialized to false
                int size = dfs(mat, n, m, i, j, visited) % 10;
                char str[2];
                char* size_c = str;
                sprintf(size_c, "%d", size);
                mat[i*m + j] = size_c[0];
            }
        }
    }
    end = timeclock::now();
    cout << "dfs time: " << mil(end - start).count() << "\n";

    start = timeclock::now();
    // Output modified matrix
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            printf("%c", mat[i*m +j]);
        }
        printf("\n");
    }
    end = timeclock::now();
    cout << "output time: " << mil(end - start).count() << "\n";

    return 0;
}

