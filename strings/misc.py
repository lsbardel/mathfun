

def altered_sos(S):
    count = 0
    for i in range(0, len(S), 3):
        for a, b in zip(S[i:3+i], 'SOS'):
            count += (a != b)
    return count


def funny_string(S):
    """A string is funny if

    S[i]-S[i-1] == R[i]-R[i-1]  for all i > 0

    where R is the reverse of S
    """
    S = S.lower()
    R = ''.join(reversed(S))
    for i, s in enumerate(S[1:], 1):
        d1 = abs(ord(S[i-1]) - ord(s))
        d2 = abs(ord(R[i-1]) - ord(R[i]))
        if d2 != d1:
            return False
    return True


if __name__ == '__main__':
    print(funny_string('acxz'))
