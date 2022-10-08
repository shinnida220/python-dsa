# SORTING

Rearranging elements, changing the order of elements in a list. Could be in asc / desc

## Bubble Sort - Naive approach

- Pick one item and compare with all others

## Efficiency

Worst case - O(n^2)
Bestt case - O(n)
*Sorting is In-Place, we don't need any extra data structure
*low space complexity, we are not copying any data to any where

For n number of elements
we run through each items all the

## Merge Sort O(nlog(n))

To sort an array, divide it into two halves, sort the two halves (recursively), and then merge the results.

Time complexity -> better than bubble sort
Aux Space -> More space O(n) Linear

You split a huge array down as much as possible and over time built it back up, doing your comparism at each step of the way
(Divide and Conquer)

n comparisms at n steps

## QUICK SORT -> https://visualgo.net/en/sorting/

One of the most efficient sorting algorithm

- You pick a random number (pivot) (usually element at end)
- move all values above it to left, and other to right
-

Worse Case -> O(n^2)
Average -> O(nlog(n))

Not good for near sort array

Optimisation

### The Idea of QuickSort

Quicksort is a fast sorting algorithm that works by splitting a large array of data into smaller sub-arrays. This implies that each iteration works by splitting the input into two components, sorting them, and then recombining them. For big datasets, the technique is highly efficient since its average and best-case complexity is O(n\*logn).

It was created by Tony Hoare in 1961 and remains one of the most effective general-purpose sorting algorithms available today. It works by recursively sorting the sub-lists to either side of a given pivot and dynamically shifting elements inside the list around that pivot.

As a result, the quick sort method can be summarized in three steps:

- Pick: Select an element.
- Divide: Split the problem set, move smaller parts to the left of the pivot and larger items to the right.
- Repeat and combine: Repeat the steps and combine the arrays that have previously been sorted.

### Benefits of Quicksort

Let’s go through a few key benefits of using Quicksort:

It works rapidly and effectively.
It has the best time complexity when compared to other sorting algorithms.
Quick sort has a space complexity of O(logn), making it an excellent choice for situations when space is limited.

### Limitations of Quicksort

- Despite being the fastest algorithm, QuickSort has a few drawbacks. Let’s have a look at some of the drawbacks of Quicksort.
- This sorting technique is considered unstable since it does not maintain the key-value pairs initial order.
- When the pivot element is the largest or smallest, or when all of the components have the same size. The performance of the quicksort is significantly impacted by these worst-case scenarios.
- It’s difficult to implement since it’s a recursive process, especially if recursion isn’t available.

### Implementation

- We first partition the list based on a right and left index
- To partition, We pick a pivot (say last element on the right)
- Based on pivot, we move all elements lesser than pivot to the left, greater or equal to the right. We are not worried about the orders yet

```
Say we have the list
arr = [3, -2, -1, 0, 2, 4, 1]

we define a quick_sort function (qs), such that

def qs(arr, l, r):
    # Base case
    if l >= r:
        return

    # we create a partion.
    # The goal of this partition is to
    # - move the selected pivot to the middle
    # - move values lesser than pivot to left of pivot
    # - move values greater than pivot to right of pivot
    p = partition(arr, l, r)

    # then we quick-sort the left and right elements
    qs(arr, l, p-1)
    qs(arr, p+1, r)
```

For Partitioning (given an array starting with bounds -> x,y)

- we choose a pivot at y, pivot = arr[y]
- declare 2 indices i and j, j is the current element we are checking
- i will start at x-1, j at i+1
- if value at j is less than pivot, increment i, swap values at i and j and increment i
- if value at j is greater/equal than pivot, we ignore it and increment j by 1
- Do this until j reaches pivot
- Now finally move pivot to i+1, and swap pivot and i
- At this point, all elements on left on pivot will be lesser than pivot and all element on its right higher or equal to it. They may not be sorted, but its fine
- Next we return the pivot index, and then pass all elements to the left of pivot to quick sort and all elements to its right to quicksort.
