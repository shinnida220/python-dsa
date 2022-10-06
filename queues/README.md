# QUEUES

WHere elements that's added to the list first leaves first or First In First Out (FIFO). Its the opposite of a stack.
Can be implemented using a queue

Tail - Newest element
Head - First element

A reference to the teail and head can be added so that peeking at either can be in constant time

- Enqueue - add to list
- DeQueue - remove from list (head)
- Peek - Look at the head but dont remove it

Types

- Double Deck: Double ended queue is a queue that goes both ways. You can enqueue or dequeue from either end
  More like
- Priority Queue - Elements are added by priroty. At point of dequeuing, elements with highest priority are removed first.
  E.g [A prio 1 | B prio 2 | C prio 2] -> A is dequeued first

Can be implemented using deque from collections

```
    >>> from collections import deque
    >>> queue = deque(["Eric", "John", "Michael"])
    >>> queue.append("Terry")           # Terry arrives
    >>> queue.append("Graham")          # Graham arrives
    >>> queue.popleft()                 # The first to arrive now leaves
    'Eric'
    >>> queue.popleft()                 # The second to arrive now leaves
    'John'
    >>> queue                           # Remaining queue in order of arrival
    deque(['Michael', 'Terry', 'Graham'])
```
