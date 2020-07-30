def solution(S):
    p = ""
    N = 0
    for s in S:
        p += s
        unique = set()
        for k in range(1, 1 + len(p)):
            c = p[-k]
            if c in unique:
                unique.remove(c)
            else:
                unique.add(c)
            N += 1 if len(unique) == k % 2 else 0

    return N


def test():
    assert solution("02002") == 11
    assert solution("09345") == 5
    assert solution("09355") == 7
    assert solution("00000") == 15


if __name__ == "__main__":
    import sys

    S = sys.argv[1]
    if S == "test":
        test()
    else:
        print(solution(S))
