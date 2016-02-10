/*
 * Mergesort implementation
 *
 * Author: Jonathan Johnston
 * Date: 2016/2/9
 */
#include <iostream>

/*
 * Merge two sorted sections of an array.
 */
void merge(int* arr, int left, int middle, int right)
{
    int size = right - left + 1;
    int merge_arr[size];
    int l_idx = left, r_idx = middle + 1;

    // move indices across left and right halves, copying the smallest
    // value of the two, or the rest of the half that is within index bounds
    for (int i = 0; i < size; ++i) {
        if (l_idx < middle + 1 && r_idx < right + 1) {
            merge_arr[i] = (arr[l_idx] <= arr[r_idx]) ? 
                arr[l_idx++] : arr[r_idx++];
        } else {
            merge_arr[i] = (l_idx < middle + 1) ? arr[l_idx++] : arr[r_idx++];
        }
    }

    // copy sorted merge array into input array
    for (int i = 0; i < size; ++i) {
        arr[left + i] = merge_arr[i];
    }

    return;
}

/*
 * Mergesort algorithm on an integer array given left and right bounds.
 */
void mergesort(int* arr, int left, int right)
{
    if ((right - left) <= 0) return;

    int middle = (left + right) / 2;
    mergesort(arr, left, middle);
    mergesort(arr, middle + 1, right);
    merge(arr, left, middle, right);
    return;
}

int main()
{
    int size;
    int* arr;
    int test1[] = {2, 0, 1, 5, 3, 7, 6, 4, 4, 1, 13, 12, 18, 20, 99, 3, 17};
    int test2[] = {0};
    int test3[] = {1, 2, 3, 4, 5};
    int test4[] = {5, 4, 3, 2, 1};
    int sizes[] = {17, 1, 5, 5};
    int* test_cases[] = {test1, test2, test3, test4};

    for (int j = 0; j < 4; ++j) {
        arr = test_cases[j];
        size = sizes[j];

        std::cout << "unsorted array:\n";
        for (int i = 0; i < size; ++i) {
            std::cout << arr[i] << ", ";
        }
        std::cout << "\n";

        mergesort(arr, 0, size - 1);

        std::cout << "sorted array:\n";
        for (int i = 0; i < size; ++i) {
            std::cout << arr[i] << ", ";
        }
        std::cout << "\n\n";
    }

    return 0;
}
