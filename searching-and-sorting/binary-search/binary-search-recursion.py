"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list.

Visualizer here -> https://www.cs.usfca.edu/~galles/visualization/Search.html
"""

""" Recursive approach """


def binary_search(input_array, value):
    return _binary_search(input_array, value, 0, len(input_array) - 1)


def _binary_search(input_array, value, left, right):
    """Your code goes here."""
    # base case
    if right >= left:
        middle = (right + left) // 2

        if input_array[middle] == value:
            return middle
        elif input_array[middle] > value:
            right = middle - 1
            return _binary_search(input_array, value, left, right)
        else:
            left = middle + 1
            return _binary_search(input_array, value, left, right)
    else:
        return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15

print(str(binary_search(test_list, test_val1)))
print(str(binary_search(test_list, test_val2)))
