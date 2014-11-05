from prime_numbers import prime_numbers


def factors(prime):
    factors = set([1])
    for i, p in enumerate(prime):
        c = p
        for n in prime[i+1:]:
            c *= n
            factors.add(p*n)
            factors.add(c)
    return list(sorted(factors))


def triangle_factors(num):
    primes = prime_numbers(num)
    while True:
        pn1 = prime_factors(n+1)
        pf = pn + pn1
        pf.remove(1)
        pf.remove(2)
        all = factors(pf)
        if len(all) > num:
            break
        n += 1
        pn = pn1
    return n * (n + 1) // 2



if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 500
    print(triangle_factors(num))