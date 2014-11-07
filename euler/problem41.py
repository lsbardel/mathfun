from mathfun.prime_numbers import is_prime


def problem41():
    cache = {}
    for number in range(999999999, 1, -1):
        snumber = str(number)
        if '0' in snumber or len(set(snumber)) < len(snumber):
            continue
        print('%d, cache size %d' % (number, len(cache)))
        if is_prime(number, cache):
            return number


if __name__ == '__main__':
    import time
    start = time.time()
    print(problem41())
    print('%s seconds' % (time.time() - start))

