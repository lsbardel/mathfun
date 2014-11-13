from functools import reduce


def problem92(number=10000000):
    done = (1, 89)
    total = 0
    cache = {}
    for n in range(2, number):
        process = []
        while n not in done:
            if n in cache:
                n = cache[n]
            else:
                process.append(n)
                n = reduce(lambda x, y: x + int(y)**2, str(n), 0)
        for p in process:
            cache[p] = n
        total += 1 if n == 89 else 0
    return total


if __name__ == '__main__':
    print(problem92())
