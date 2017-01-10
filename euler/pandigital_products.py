"""https://projecteuler.net/problem=32
"""
import time

def pandigital_products():
    found = set()
    for i in range(2, 100):
        if i < 10:
            start = 1234
        else:
            start = 123
            if not i % 10:
                continue
            si = str(i)
            if si[0] == si[1]:
                continue
        for j in range(start, 10000//i):
            prod = i*j
            if not '123456789'.strip('%s%s%s' % (i, j, prod)):
                found.add(prod)
    return sum(found)


if __name__ == '__main__':
    start = time.monotonic()
    result = pandigital_products()
    print('time: %.4f, result: %d' % (time.monotonic()-start, result))
