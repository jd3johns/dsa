# Data Structures and Algorithms in C++ and Python

## Completed

### Graphs

* Dijkstra's single-source shortest-paths algorithm: [Python](python/graphs/dijkstra.py)

### Sorting

* Mergesort: [Python](python/sorting/mergesort.py)
* Heapsort: [Python](python/sorting/heapsort.py)
* Bubble sort: [Python](python/sorting/bubble_sort.py)

### Searching

* Breadth-first search on a graph: [Python](python/searching/bfs.py)
* Depth-first search on a graph: [Python](python/searching/dfs.py)
* Binary search on an array: [Python](python/searching/binary_search.py)

### Stacks and Queues

* Implementation of a queue using two stacks: [Python](python/stacks_and_queues/queue_of_stacks.py)
* Simple queue implementation: [Python](python/stacks_and_queues/queue.py)
* Simple stack implementation: [Python](python/stacks_and_queues/stack.py)

### Linked Lists

* Linked list removal of node in middle of list: [Python](python/linked_lists/remove_node.py)
* Linked list duplicate node removal: [Python](python/linked_lists/remove_duplicates.py)
* Linked list node implementation: [Python](python/linked_lists/node.py)

### Strings

* C-string reverse: [C++](cpp/strings/reverse.cpp)
* String permutation check: [Python](python/string/is_permutation.py)
* String rotation check: [Python](python/string/is_rotation.py)
* Simple string compress: [Python](python/string/string_compress.py), [C++](cpp/strings/string_compress.cpp)
* String replace: [Python](python/string/string_replace.py)

### Miscellaneous

* Codeforces Problem 1A ("Theatre Square"): [C++](cpp/misc/theatre_square.cpp)
* Data type size listing: [C++](cpp/misc/list_data_type_sizes.cpp)
* String concatenation benchmark: [C++](cpp/misc/string_concat_benchmark.cpp)
* FizzBuzz: [C++](cpp/misc/fizzbuzz.cpp)
* Standing ovation: [Python](python/misc/standing_ovation.py)
* Vietnam snake: [Python](python/misc/vietnam_snake.py)

## Unit Tests

Python unit tests kept alongside target files in subdirectories, so to run all unit tests within a category:

```
cd target_directory
python -m unittest discover --pattern=test*.py
``` 

## Code Formatting

I use the [Google Python style guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html) to format my Python code, and pylint as a quick tool to check adherence to the formatting style.

Install pylint on Debian/Ubuntu and run it on Python source:

```
sudo apt-get install pylint
pylint source.py
```
