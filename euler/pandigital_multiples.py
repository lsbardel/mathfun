"""https://projecteuler.net/problem=38
"""

def pandigital_multiples():
    for i in range(9876, 9213-1, -1):
        j = 2*i
        num = '%s%s' % (i, j)
        if len(num) == 9 and not '123456789'.strip(num):
            return int(num)


if __name__ == '__main__':
    import time
    start = time.monotonic()
    result = pandigital_multiples()
    print('time: %.4f, result: %d' % (time.monotonic()-start, result))
