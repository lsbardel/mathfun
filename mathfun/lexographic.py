"""
Next lexicographical permutation algorithm

https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""


def next_lexo(S):
    b = S[-1]
    for i, a in enumerate(reversed(S[:-1]), 2):
        if a < b:
            # we have the pivot a
            for j, b in enumerate(reversed(S), 1):
                if b > a:
                    F = list(S)
                    F[-i], F[-j] = F[-j], F[-i]
                    F = F[: -i + 1] + sorted(F[-i + 1 :])
                    return "".join(F)
        else:
            b = a
    return "no answer"
