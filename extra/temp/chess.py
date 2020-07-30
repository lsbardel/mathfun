import math


def chess(W, B):
    c = 2
    while N > 1:
        c = 3 - c
        n = math.floor(math.log(N) / math.log(2))
        m = 2 ** n
        if m == N:
            return c if n % 2 else 3 - c
        N -= m
    return c


if __name__ == "__main__":
    print(chess([["N", "B", 2], ["Q", "B", 1]], [["Q", "A", 1]]))
