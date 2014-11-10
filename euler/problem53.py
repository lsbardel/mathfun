from math import factorial


def problem53(N=100, T=1000000):
    total = 0
    for n in range(2, N+1):
        r = n // 2
        nf = factorial(n)
        if nf/(factorial(r)*factorial(n-r)) > T:
            total += 1 + n % 2
            r -= 1
            while nf/(factorial(r)*factorial(n-r)) > T:
                total += 2
                r -= 1
    return total


if __name__ == '__main__':
    print(problem53())



