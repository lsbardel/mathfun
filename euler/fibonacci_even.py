

def even_fibonacci(limit):
    if not limit:
        return 0
    total, a, b = 0, 0, 1
    while b <= limit:
        if not b % 2:
            total += b
        a, b = b, b + a
    return total


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 4000000
    print(even_fibonacci(num))

