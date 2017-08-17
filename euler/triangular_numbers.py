from mathfun.primes import factors


def triangular_number():
    n = 100
    cache = {}
    while True:
        t = n*(n + 1) // 2
        f = factors(t, cache)
        N = len(f)
        if N >= 501:
            return t


if __name__ == '__main__':
    print(triangular_number())
