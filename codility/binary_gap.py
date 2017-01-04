from functools import reduce


def solution(N):
    if N < 5:
        return 0
    gaps = bin(N)[2:].split('1')
    gaps.pop()
    return reduce(lambda a, b: max(len(b), a), gaps, 0)
