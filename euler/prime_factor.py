"""https://projecteuler.net/problem=3
"""


def largest_prime_factor(number):
    if number <= 3:
        return number

    result = []
    while number > 2 and not number % 2:  # remove powers of twos
        number //= 2
        result.append(2)
    f = 3
    while f*f < number:
        while not number % f:
            result.append(f)
            number = number // f
        f += 2  # we have already dealt with
    result.append(number)
    return result


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 600851475143
    print(largest_prime_factor(num))
