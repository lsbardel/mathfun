from functools import reduce
from itertools import combinations


def lucky_number_8_very_slow(number):
    count = 0
    for n in range(1, len(number) + 1):
        count = reduce(
            lambda a, b: a + (not (int("".join(b)) % 8)), combinations(number, n), count
        )
    return count % (10 ** 9 + 7)


def lucky_number_8(number):
    count = 0
    stack = []
    for n in reversed(number):
        m = int(n)
        count += not (m % 8)

        for v in stack:
            count += not (int(n + v) % 8)

        if not (m % 2):
            stack.append(n)

    return count % (10 ** 9 + 7)


if __name__ == "__main__":
    print(lucky_number_8("968"))
    import time
    from random import randint

    number = "".join((str(randint(0, 9)) for _ in range(10)))
    print(number)
    start = time.monotonic()
    value = lucky_number_8(number)
    delta = time.monotonic() - start
    print("result %d in %.4f seconds" % (value, delta))
