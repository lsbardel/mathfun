

def pandigital_prime():
    test = '1234567'
    for x in range(7654321, 0, -1):
        if not x % 2 or not x % 3 or not x % 5:
            continue
        xs = str(x)
        if len(xs) < len(test):
            test = ''.join(range(1, len(xs)+1))
        if not test.strip(xs):
            i = 5
            w = 2

            while i * i <= x:
                if x % i == 0:
                    x = 0
                    break
                i += w
                w = 6 - w

            if x:
                return x


if __name__ == '__main__':
    import time
    start = time.monotonic()
    result = pandigital_prime()
    print('time: %.4f, result: %d' % (time.monotonic()-start, result))
