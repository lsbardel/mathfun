

def solution(S):
    # write your code in Python 2.7
    o = 0
    for i, s in enumerate(S, 1):
        o += s == '('
        c = 0
        for g in S[i:]:
            c += g == ')'
        if o == c:
            return i



if __name__ == '__main__':
    assert solution('(())))(') == 4
