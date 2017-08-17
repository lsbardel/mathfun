"""https://projecteuler.net/problem=493

E(X)
= E(X0+X1+...+X6)
= E(X0) + E(X1) + ... + E(X6)        by linearity of expectation
= 7*E(X0)                            by symmetry
= 7 * probability that a particular color is present
= 7 * (1- probability that a particular color is absent)
= 7 * (1 - (# ways to pick 20 avoiding a color)/(# ways to pick 20))
= 7 * (1 - (60 choose 20)/(70 choose 20))
"""
from math import exp, lgamma


def factorial(lo, hi):
    if lo + 1 < hi:
        mid = (hi + lo) // 2
        return factorial(lo, mid)*factorial(mid+1, hi)
    if lo == hi:
        return lo
    return lo*hi


def colors():
    return 7*(1 - factorial(41, 50)/factorial(61, 70))


def colors2():
    return 7*(1 - exp(lgamma(61) - lgamma(41) + lgamma(51) - lgamma(71)))


if __name__ == '__main__':
    print(round(colors(), 9))
    print(round(colors2(), 9))
