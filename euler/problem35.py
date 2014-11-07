from itertools import permutations

from mathfun.prime_numbers import is_prime


def circular_primes(number=1000000):
    cache = {}
    count = 0
    primes = 0
    for n in range(2, number):
        if is_prime(n, cache):
            primes += 1
            circ = True
            snum = str(n)
            N = len(snum)
            for i in range(1, N):
                num = int(snum[i:] + snum[:i])
                if not is_prime(num, cache):
                    circ = False
                    break
            if circ:
                print(n)
                count += 1
    return primes, count


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 1000000
    print('primes: %d, circular: %d' % circular_primes(num))

