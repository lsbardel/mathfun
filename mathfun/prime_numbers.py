from math import sqrt, ceil


def is_prime(number):
    '''Check if a number is a prime number'''
    if number <= 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9: # already excluded 4, 6 & 8
        return True
    elif number % 3 == 0:
        return False
    else:
        limit = int(sqrt(number)) # so that f*f <= number
        f = 5
        while f <= limit:
            if number % f == 0:  # 6k-1
                return False
            if number % (f+2) == 0: #6k+1
                return False
            f += 6
    return True


def prime_factors(number, cache=None):
    '''Return all prime factors of number.

    For example::

        prime_factors(18) = [2, 3, 3]

    Cache is a dictionary which can be used to speedup repeted evaluations
    '''
    if number <= 1:
        return []
    elif number <= 3:
        return [number]
    else:
        if cache is None:
            cache = {}
        elif number in cache:
            return cache[number]
        all = []
        while number % 2 == 0:
            all.append(2)
            number = number // 2
            if number in cache:
                all.extend(cache[number])
                return all
        while number % 3 == 0:
            all.append(3)
            number = number // 3
            if number in cache:
                all.extend(cache[number])
                return all
        f = 5
        while f <= int(sqrt(number)):
            while number % f == 0:
                all.append(f)
                number = number // f
                if number in cache:
                    all.extend(cache[number])
                    return all
            while number % (f+2) == 0:
                all.append(f+2)
                number = number // (f+2)
                if number in cache:
                    all.extend(cache[number])
                    return all
            f += 6
        if number != 1:
            # this is always a prime number, adde it to the cache
            cache[number] = [number]
            all.append(number)
    return all


def factors(number, cache=None):
    primes = prime_factors(number, cache)
    all = set(primes)
    all.add(1)
    for i, p in enumerate(primes):
        row = primes[i+1:] + primes[0:i]
        remaining = row
        while remaining:
            f = []
            for v in remaining:
                f.append(p*v)
            all.update(f)
            p = f[0]
            remaining = remaining[1:]
    all.discard(number)
    return all

