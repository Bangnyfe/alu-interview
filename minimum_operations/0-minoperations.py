#!/usr/bin/python3
"""Module for minimum operations problem."""


def minOperations(n):
    """Calculate minimum operations to get n H characters.

    Args:
        n: Target number of H characters

    Returns:
        Minimum number of operations needed, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Find prime factors and sum them
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
