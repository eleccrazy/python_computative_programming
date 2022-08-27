#!/usr/bin/python3

def combination_two(n):
    """ This function uses the concept of recursion to solve the given problem."""
    
    # If the input is not integer we should have to raise a type error
    if not isinstance(n, int):
        raise TypeError("The Number of pets must be integer!")

    # If the value of n is negative we should have to raise a value error
    if n < 0:
        raise ValueError("The Number of pets can't be negative")

    if n < 2:
        return n

    n += 1

    def helper(n):
        if n < 2:
            return n
        else:
            return helper(n - 1) + helper(n - 2)
    return helper(n)
