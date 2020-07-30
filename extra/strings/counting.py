def solution(S):
    """Find the position on a string S formed by a set of two characters
    such that, the number of of one characters on the left is equal
    to the number of the same characters on the right.

    (())))(
    abbaaab => 4 (abba, aab)
    """
    o = 0
    for i, s in enumerate(S, 1):
        o += s == "("
        c = 0
        for g in S[i:]:
            c += g == ")"
        if o == c:
            return i
