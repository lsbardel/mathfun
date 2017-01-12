

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    import sys
    argv = sys.argv
    print(gcd(int(argv[1]), int(argv[2])))
