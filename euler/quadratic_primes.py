from mathfun.primes.prime_numbers import is_prime


def quadratic_primes():
    cache = {}
    best = 0
    prod = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while is_prime(n*(n + a) + b, cache):
                n += 1
            if n > best:
                best = n
                prod = (a, b)
    return best, prod[0], prod[1], prod[0]*prod[1]


if __name__ == '__main__':
    print(quadratic_primes())
