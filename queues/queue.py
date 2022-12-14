"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""

from collections import deque


class Queue:
    def __init__(self, head=None):
        self.storage = deque([head])

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def dequeue(self):
        return self.storage.popleft()


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(str(q.peek()))

# Test dequeue
# Should be 1
print(str(q.dequeue()))

# Test enqueue
q.enqueue(4)
# Should be 2
print(str(q.dequeue()))
# Should be 3
print(str(q.dequeue()))
# Should be 4
print(str(q.dequeue()))
q.enqueue(5)
# Should be 5
print(str(q.peek()))
