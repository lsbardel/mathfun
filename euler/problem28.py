"""https://projecteuler.net/problem=28
"""


def problem28(number):
    s = 1
    total = s
    for n2 in range(2, number, 2):
        for _ in range(4):
            s += n2
            total += s
    return total


if __name__ == '__main__':
    print(problem28(1001))
