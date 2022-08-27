#!/usr/bin/python3

def combination(n):
    """
    This python function computes all distinct combinations the employee
    can bring the pets to work.
    """

    # Approaching a problem:
    # solution(1) = 1
    # solution(2) = 2
    # solution(3) = 3
    # solution(4) = 5
    # solution(5) = 8
    # solution(6) = 13
    # solution(7) = 21
    # and soon...
    # 
    # From the above expectation results, we can clearly see that the output result
    # is basically a fibonacci series. Using this assumption, we can simply write
    # the logic as follows.

    first = 0
    second = 1

    # If the input is not integer we should have to raise a type error
    if not isinstance(n, int):
        raise TypeError("The Number of pets must be integer!")

    # If the value of n is negative we should have to raise a value error
    if n < 0:
        raise ValueError("The Number of pets can't be negative")

    if n < 2:
        return n
    else:
        n += 2
        i = 2
        while i < n:
            temp = first + second
            first = second
            second = temp
            i += 1
        return second
