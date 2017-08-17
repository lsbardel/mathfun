

def tobase(n, b):
    num = []
    while n:
        r = n % b
        n //= b
        if r < 0:
            r -= b
            n += 1
        num.append(r)
    return ''.join((str(s) for s in reversed(num)))


if __name__ == '__main__':
    print(tobase(5, 2))
    print(tobase(10, 2))
    print(tobase(10, 3))
    print(tobase(8, 3))
    print(tobase(10, -2))
