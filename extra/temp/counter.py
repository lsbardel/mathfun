import math


def counter(N):
    c = 2
    while N > 1:
        c = 3 - c
        n = math.floor(math.log(N) / math.log(2))
        m = 2 ** n
        if m == N:
            return c if n % 2 else 3 - c
        N -= m
    return c


def pairs(a, k):
    # a is the list of numbers and k is the difference value
    a = sorted(a)
    N = len(a)
    answer = 0
    for i, v in enumerate(a[:-1]):
        D = (N - i + 1) // 2
        j = i + D
        while D:
            d = a[j] - v
            if d == k:
                answer += 1
                break
            D //= 2
            if d > k:
                j -= D
            else:
                j += D
    return answer


if __name__ == "__main__":
    print(pairs([1, 5, 3, 4, 2], 2))
