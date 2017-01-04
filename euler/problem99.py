"""https://projecteuler.net/problem=99
"""
from math import log


def largest_exponentail(numbers):
    val = 0
    imax = 0
    for i, ba in enumerate(numbers, 1):
        v = ba[1]*log(ba[0])
        if v > val:
            val = v
            imax = i
    return imax


if __name__ == '__main__':
    import requests
    text = requests.get(
        'https://projecteuler.net/project/resources/p099_base_exp.txt'
    ).text
    numbers = [[int(l) for l in line.split(',')] for line in text.split('\n')]
    print(largest_exponentail(numbers))
