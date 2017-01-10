
def solution(A):
    """Negative of base-2 numbers
    """
    b = 1
    x = 0
    B = []
    for a in A:
        x += a*b
        b *= -2
    x = -x
    while x:
        B.append(x % 2)
        x = -(x // 2)
    return B


if __name__ == '__main__':
    assert solution([1, 0, 0, 1, 1]) == [1, 1, 0, 1]
    assert solution([1, 0, 0, 1, 1, 1]) == [1, 1, 0, 1, 0, 1, 1]

