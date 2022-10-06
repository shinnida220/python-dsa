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


def get_fib(position):
    return _get_fib(position)


def _get_fib(position, ):
    if position == 0 or position == 1:
        return position

    return _get_fib(position - 2) + _get_fib(position - 1)


# Test cases
print(str(get_fib(9)))
print(str(get_fib(11)))
print(str(get_fib(0)))
