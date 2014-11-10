from mathfun.utils import zip


def problem112():
    bouncy = 0
    total = 100
    while float(bouncy)/total < 0.99:
        total += 1
        bouncy += 1 if isbouncy(total) else 0
    return total


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


if __name__ == '__main__':
    print(problem112())
