from itertools import izip
from math import sqrt


def solution(A, B):
    # write your code in Python 2.7
    cache = {}
    count = 0
    for a, b in izip(A, B):
        a = set(prime_factors(a, cache))
        b = set(prime_factors(b, cache))
        count += a == b
    return count


def prime_factors(number, cache):
    if number in cache:
        return cache[number]
    elif number <= 1:
        return []
    elif number <= 3:
        return [number]
    else:
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
            while number % (f+2) == 0:
                result.append(f+2)
                number //= (f+2)
                if number in cache:
                    result.extend(cache[number])
                    return result
            f += 6
        if number != 1:
            # this is always a prime number, add it to the cache
            cache[number] = [number]
            result.append(number)
    return result


if __name__ == '__main__':
    solution([15], [75])
