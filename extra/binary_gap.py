from functools import reduce


def solution(N):
    if N < 5:
        return 0
    gaps = bin(N)[2:].split('1')
    gaps.pop()
    return reduce(lambda a, b: max(len(b), a), gaps, 0)


def count_div(A, B, K):
    k1 = A // K - 1 + A % K
    k2 = B // K
    return max(k2 - k1, 0)


def triangle(A):
    pass


if __name__ == '__main__':
    assert count_div(1, 10, 3) == 3
    assert count_div(0, 0, 3) == 1
    assert count_div(0, 3, 3) == 2
    assert count_div(3, 10, 3) == 3
    assert count_div(3, 9, 3) == 3
    assert count_div(1, 10, 1) == 10
