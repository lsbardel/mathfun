"""https://projecteuler.net/problem=112
"""


def isbouncy(number):
    snumber = str(number)
    bouncy = False
    for a, b in zip(snumber, snumber[1:]):
        if int(b) < int(a):
            bouncy = True
            break
    if bouncy:
        bouncy = False
        for a, b in zip(snumber, snumber[1:]):
            if int(b) > int(a):
                bouncy = True
                break
    return bouncy


def problem112():
    bouncy = 0
    total = 100
    while bouncy/total < 0.99:
        total += 1
        bouncy += 1 if isbouncy(total) else 0
    return total


if __name__ == '__main__':
    print(problem112())
