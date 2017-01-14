"""Euclid's Algorithm
"""


def gcd(a: int, b: int) -> int:
    """Greatest common divisor

    In python 3.5 there is a function in the standard lib:

    import math
    math.gcd(a, b)
    """
    while b:
        a, b = b, a % b
    return a


def xgcd(a: int, b: int) -> tuple:
    """Extended Euclidean (GCD) algorithm

    gcd(a, b) = u*a + v*b

    Returns gdc, u, v
    """
    x, x1, y, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
    return a, x, y


if __name__ == '__main__':
    import sys
    argv = sys.argv
    print(xgcd(int(argv[1]), int(argv[2])))
