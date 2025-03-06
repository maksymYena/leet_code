"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        middle_value = (left + right) // 2
        if middle_value * middle_value == x:
            return middle_value
        elif middle_value * middle_value < x:
            left = middle_value + 1
        else:
            right = middle_value - 1

    return int(right)


print(mySqrt(x=8))
