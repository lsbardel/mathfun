

def pow2combos(n):
    c = 1
    p = 1
    while n > 1:
        c += 1
        n //= 2
        if not n % 2:
            c += 1
    return c


if __name__ == '__main__':
    print(pow2combos(1))
    print(pow2combos(2))
    print(pow2combos(3))
    print(pow2combos(4))
    print(pow2combos(10))
