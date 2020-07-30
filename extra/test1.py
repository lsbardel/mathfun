from random import randint


def solution(A):
    n = len(A)
    if not A:  # empty list
        return -1
    s = 0
    for i, v in enumerate(A):
        s += v
        A[i] = s
    result = []
    for i, s in enumerate(A):
        left = A[i - 1] if i else 0
        right = A[n - 1] - A[i]
        if left == right:
            result.append(i)
    return result if result else -1


test1 = [-1, 3, -4, 5, 1, -6, 2, 1]
test2 = [randint(-2100100100, 2100100100) for _ in range(100)]
test3 = [randint(-2100100100, 2100100100) for _ in range(1000)]
test4 = [randint(-2100100100, 2100100100) for _ in range(10000)]


if __name__ == "__main__":
    from timeit import Timer

    assert solution(test1) == [1, 3, 7]
    assert solution([]) == -1
    print(
        Timer("solution(test1)", "from __main__ import solution, test1").timeit(
            number=1000
        )
    )
    print(
        Timer("solution(test2)", "from __main__ import solution, test2").timeit(
            number=1000
        )
    )
    print(
        Timer("solution(test3)", "from __main__ import solution, test3").timeit(
            number=1000
        )
    )
    print(
        Timer("solution(test4)", "from __main__ import solution, test4").timeit(
            number=1000
        )
    )
