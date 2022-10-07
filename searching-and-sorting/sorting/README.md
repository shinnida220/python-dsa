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
