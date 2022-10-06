from turtle import pos


# function getFib(position) {
#     if (position == 0) {return 0
#                         }
#     if (position == 1) {return 1
#                         }
#     var first = 0,
#     second = 1,
#     next = first + second
#     for (var i=2
#          i < position
#          i++) {
#         first = second
#         second = next
#         next = first + second
#     }
#     return next
# }


"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

"""
You may have noticed that this solution will 
compute the values of some inputs more than 
once. 
For example get_fib(4) calls get_fib(3) and get_fib(2), 
get_fib(3) calls get_fib(2) and get_fib(1) etc. 

The number of recursive calls grows exponentially with n.

In practice if we were to use recursion 
to solve this problem, we should use a hash table 
to store and fetch previously calculated 
results. This will increase the space needed 
but will drastically improve the runtime efficiency.
"""


def get_fib(position):
    return _get_fib(position)


def _get_fib(position):
    if position == 0 or position == 1:
        return position

    return _get_fib(position - 2) + _get_fib(position - 1)


def get_fib2(position):
    return _get_fib_hash(position)


def _get_fib_hash(position, memo={}):
    if position in memo.keys():
        return memo[position]

    if position == 0 or position == 1:
        return position

    memo[position] = _get_fib_hash(
        position - 2, memo) + _get_fib_hash(position - 1, memo)
    return memo[position]


# Test cases
print(str(get_fib(9)))
print(str(get_fib(11)))
print(str(get_fib(0)))
print(str(get_fib2(100)))
