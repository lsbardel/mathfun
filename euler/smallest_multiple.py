from functools import reduce
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def smallest_multiple(number):
    return reduce(lcm, range(1, number+1))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 20
    print(smallest_multiple(num))
