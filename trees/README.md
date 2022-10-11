# TREES

Tree is a data structure that stores data in form of a tree. It starts of with at a point called root. Data is then stored across different nodes called branches

- It is an extenstion of a LinkedList
- First element is called the root, instead of one next element, it can have multiples
- No cycling allowed (no way to encounter a node twice)
- Trees are drawn vertically
- Individual elements with data is called a node
- Root is at level 1, children are only allowed one parent

## EXPLANATION

A tree can be described in the form of levels -> how many connections it takes to reach the root plus one (+1)

- Nodes are described to have both a parent-child relationship (Ancestor/Descendant)
- Sibling -> nodes at the same level
- External nodes/Leaf -> are nodes without children node
- Internal Node/Parent node
- Connections are called edges, a group of connections taken together are called a path
- Height of a node is the number of edges between that node and the furthest leaf on the tree
- Leaf has a height of Zero (0), but its parent has a height of one (1)
- Height of a tree overall is the height of the root node
- Depth of a tree is the number of edges to the root
- Height moves inversely to Depth

## DEMONSTRATION

```
        [A]
        /  \
       [B] [C]
       / \
     [D] [E]
            \
            [F]
```

Level of D => 3
Parent of C => A
Height of B => 2
Depth of F => 3

## TRAVERSAL Principle

- DFS (Depth First Search -> Child nodes are visited first)
- BFS (Breadth First Search -> Nodes at same level are visited at the same time)

Level Order Traversal

### DFS

- Pre-Order
  Check off a node as soon as you see it, before you traverse any further in the tree
- In-Order
  Check of a node until u meet a leaf, then parent
- Post-Order
  We wont be able to check off a node until we have checked of all its children

## BINARY TREES

A tree in which the parent node has at most 2 children
Nodes can have 0,1 or 2 children

Search
O(n) no tricks, we have to check all the nodes to find the node we are looking for

Delete
O(n) as we have to move some nodes around

Insert

### BST - Binary Search Tree

Binary Search Trees are sorted. Every element on the left is less than those on the right.

Unbalanced -> When the child distribution is not balanced
