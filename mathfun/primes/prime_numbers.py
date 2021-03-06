from functools import reduce
from itertools import combinations
from math import sqrt


def is_prime(number, cache=None):
    """Check if a number is a prime number"""
    if number <= 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:  # already excluded 4, 6 & 8
        return True
    elif number % 3 == 0:
        return False
    else:
        if cache is None:
            cache = {}
        elif number in cache:
            return cache[number]
        limit = int(sqrt(number))  # so that f*f < number
        f = 5
        while f <= limit:
            if number % f == 0:  # 6k-1
                cache[number] = False
                return False
            if number % (f + 2) == 0:  # 6k+1
                cache[number] = False
                return False
            f += 6
        cache[number] = True
        return True


def prime_factors(number, cache=None):
    """Return all prime factors of number.

    For example::

        prime_factors(18) = [2, 3, 3]

    Cache is a dictionary which can be used to speedup repeated evaluations
    """
    if number <= 1:
        return []
    elif number <= 3:
        return [number]
    else:
        if cache is None:
            cache = {}
        elif number in cache:
            return cache[number]
        result = []
        while number % 2 == 0:
            result.append(2)
            number //= 2
            if number in cache:
                result.extend(cache[number])
                return result
        while number % 3 == 0:
            result.append(3)
            number //= 3
            if number in cache:
                result.extend(cache[number])
                return result
        f = 5
        while f <= int(sqrt(number)):
            while number % f == 0:
                result.append(f)
                number = number // f
                if number in cache:
                    result.extend(cache[number])
                    return result
            while number % (f + 2) == 0:
                result.append(f + 2)
                number //= f + 2
                if number in cache:
                    result.extend(cache[number])
                    return result
            f += 6
        if number != 1:
            # this is always a prime number, add it to the cache
            cache[number] = [number]
            result.append(number)
    return result


def factors(number, cache=None):
    primes = prime_factors(number, cache)
    result = set(primes)
    result.add(1)
    for n in range(2, len(primes)):
        for combos in combinations(primes, n):
            result.add(reduce(prod, combos))
    return result


def prod(x, y):
    return x * y
