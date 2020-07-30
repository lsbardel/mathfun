from functools import lru_cache


def solution(A, B):
    return [count(a) % (2 ** b) for a, b in zip(A, B)]


@lru_cache(50000)
def count(a):
    print(a)
    if a == 1:
        return 1
    elif a == 2:
        return 2
    else:
        return count(a - 1) + count(a - 2)


solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1])

count(5)

count(6)

count(10)

# +
from functools import lru_cache


@lru_cache
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


import numpy as np


def frog_jumps(A):
    c = 1
    leaves = []
    for a in A:
        if a:
            leaves.append(c)
            c = 1
        else:
            c += 1
    leaves.append(c)
    deltas = np.array(leaves)
    j = 1
    n = 2
    steps = []
    while j <= len(A) + 1:
        steps.append(j)
        n += 1
        j = fib(n)
    steps = set(steps)
    print(steps)
    return distance(steps, deltas, [])


def distance(steps, deltas, jumps):
    for j, jump in enumerate(reversed(np.cumsum(deltas))):
        if jump in steps:
            new_jumps = jumps[:]
            new_jumps.append(jump)
            if j:
                result = distance(steps, deltas[-j:], new_jumps)
                if result:
                    return result
            else:
                return new_jumps


# -

a = np.random.randint(2, size=100000)

frog_jumps([])


# +
def game(A):
    s = A[0]
    j = 1
    c = []
    while j < Len(A):
        a = A[j]
        if a > 0:
            s += 0
            c = 0
            m = 0
        elif c < 6:
            c += 1
            m = a if c == 1 else max(a, m)
        else:
            s += m


# -

6 * [1]
