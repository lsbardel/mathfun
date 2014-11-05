from prime_numbers import factors


def amicable(limit=10000):
    # use cache for prime factors calculation
    cache = {}
    amicable_sum = 0
    for a in range(limit-1, 1, -1):
        b = sum(factors(a, cache))
        if a != b:
            if a == sum(factors(b, cache)):
                amicable_sum += a
    return amicable_sum


if __name__ == '__main__':
    import sys
    import timeit
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 10000
    t = timeit.timeit('amicable()',
                      'from __main__ import amicable',
                      number=10)
    print(t)
    print(amicable(num))
