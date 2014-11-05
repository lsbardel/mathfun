import math


def largest_prime_factor(number):
    '''Euler problem 3'''
    all = []
    if number <= 3:
        all.append(number)
        return number
    while number > 2 and not number % 2: # remove powers of twos
        number = number // 2
        all.append(2)
    f = 3
    while f*f < number:
        while not number % f:
            all.append(f)
            number = number // f
        f += 2 # we have already dealt with
    all.append(number)
    return all


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 600851475143
    print(largest_prime_factor(num))

