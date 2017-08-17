from functools import reduce
from math import gcd


def add(frac, a, b, d2):
    d1 = a / b
    if d1 == d2:
        frac.add((a, b))
        return len(frac) == 4


def digit_cancelling_fractions():
    frac = set()
    for d in range(11, 99):
        a = d // 10
        b = d % 10
        if not b:
            continue
        for n in range(a+1, 10):
            # test for a
            if add(frac, b, n, d / (10*n + b)):
                break

            # test for a
            if n == b:
                for c in range(1, 10):
                    if add(frac, a, c, d / (10*n + c)):
                        break

            elif add(frac, a, b, d / (10*n + a)):
                    break

    n = reduce(lambda a, b: a * b[0], frac, 1)
    d = reduce(lambda a, b: a * b[1], frac, 1)
    return d // gcd(n, d)


if __name__ == '__main__':
    print(digit_cancelling_fractions())
