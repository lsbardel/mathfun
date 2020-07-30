import bisect
from itertools import izip


def maxProductOfTree(A):
    """Triangular triplets"""
    A.sort()
    N = len(A)
    result = A[N - 1] * A[N - 2] * A[N - 3]
    if A[0] < 0 and A[1] < 0:
        result = max(A[0] * A[1] * A[N - 1], result)
    return result


def passingCars(A):
    east = 0
    passing = 0
    for a in A:
        if a:
            passing += east
        else:
            east += 1
    return passing


def CountTriangles(A):
    result = 0
    for i, p in enumerate(A[:-2], 1):
        for j, q in enumerate(A[i:-1], i + 1):
            for r in A[j:]:
                result += p + q > r and q + r > p and r + p > q
    return result


def isNested(S):
    # write your code in Python 2.7
    close = {")": "(", "]": "[", "}": "{"}
    open = set(close.itervalues())
    stack = []
    for c in S:
        if c in open:
            stack.append(c)
        elif c in close:
            if stack and stack.pop() == close[c]:
                continue
            return 0
    return 0 if stack else 1


def fish(A, B):
    stack = []
    for size, d in izip(A, B):
        if not stack:
            stack.append((size, d))
        else:
            size2, d2 = stack[-1]
            if d2 and not d:
                if size > size2:
                    # fish in stack eaten
                    stack.pop()
                else:
                    # current fish eaten
                    continue
            # add current fish to stack
            stack.append((size, d))
    return len(stack)
