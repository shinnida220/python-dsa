# BINARY SE

An Algorithm is a high level description of a trick for solving a problem

The idea is

- You sort the list in ascending order
- Divide the list and compare with the middle element.
- If the number in middle is greater than your number, discard the group on the RHS and repeat step 2 again on the LHS
- Else If the number in middle is lesser than your number, discard the group on the LHS and repeat step 2 again on the list on the RHS
- Repeat till you find a match or exit knowing the number doesn't exist in the collection

## EFFICIENCY

O(LOG(n) + 1) -> Base 2

```
RESULT TABLE for Binary Search
------------------------------------------------
Array Size | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
------------------------------------------------
Itirations | 0 | 1 | 2 | 2 | 3 | 3 | 3 | 3 | 4 |
```
