from itertools import permutations


def problem24(number):
    for n, p in enumerate(permutations(list(range(10)), 10), 1):
        if n == number:
            return p


if __name__ == '__main__':
    print(''.join(str(n) for n in problem24(1000000)))
