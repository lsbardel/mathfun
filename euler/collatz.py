

def collatz(n, cache):
    count = 0
    while n > 1:
        if n not in cache:
            count += 1
            n = 3*n + 1 if n % 2 else n // 2
        else:
            count += cache[n]
            n = 1
    return count


def longest_collatz(number):
    cache = {}
    max_count = 0
    max_number = 1
    for n in range(2, number):
        count = collatz(n, cache)
        cache[n] = count
        if count > max_count:
            max_count = count
            max_number = n
    return (max_number, max_count)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 1000000
    print(longest_collatz(num))