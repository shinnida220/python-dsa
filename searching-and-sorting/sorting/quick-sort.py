"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


# Sort array arr with bounds start & end
def quicksort(arr, start, end):
    # If the lower bound is less than the higher bound
    if start < end:
        # let get a pivot
        arr, pivot = partition(arr, start, end)

        # sort the left part
        arr = quicksort(arr, start, pivot-1)
        # sort the right part
        arr = quicksort(arr, pivot+1, end)

    # Return arr finally
    return arr


# The partition chooses a pivot (say last element)
# define 2 indexes, i (start-1) and j
# We compare value at index j (up until pivot) with pivot
# if less than pivot, we increment i by 1, swap i and j
# finally increase i by 1 and swap value at i and pivot
# By now, elements less than pivot should be on left and greater on right
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    j = start

    while j < end:
        if arr[j] < pivot:
            i += 1
            arr = swap(arr, i, j)
        j += 1

    # swap element at i+1 and pivot (end)
    i += 1
    arr = swap(arr, i, end)

    # We are returning the modified array and the pivot index
    # with the assumption that arr is not a global variable
    return arr, i


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr


def quicksort2(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sorted(less)+equal+sorted(greater)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test2 = [7, 2, 1, 6, 8, 5, 3, 4]
print('-- Before Sorting --')
print(test)
print(test2)
print(' ')
print('-- After Sorting --')
print(quicksort(test, 0, len(test) - 1))
print(quicksort(test2, 0, len(test2) - 1))
print('-- Using QS2 After Sorting --')
print(quicksort2(test))
print(quicksort2(test2))
