from collections import Counter


def solution(N, A):
    # write your code in Python 2.7
    counter = Counter()
    base = 0
    maxv = 0
    for a in A:
        if a > N:
            counter = Counter()
            base = maxv
        else:
            a -= 1
            v = 1 + (counter[a] or base)
            counter[a] = v
            maxv = max(maxv, v)
    return [counter[i] or base for i in range(N)]


if __name__ == "__main__":
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
