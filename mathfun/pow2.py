

def pow2(N):
    term = summation = 2
    if N > 1:
        h = N // 2
        for _ in range(2, h+1):
            term *= 2
            summation += term

        summation += term*(summation + 2*term*(N % 2))

    return summation


if __name__ == '__main__':
    assert pow2(1) == 2
    assert pow2(2) == 6
    assert pow2(3) == 14
    assert pow2(20) == 2**21 - 2
