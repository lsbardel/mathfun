

def double_base_palindromes():
    t = 1 + 3 + 5 + 7 + 9
    c = 11
    while c < 1000000:
        s = str(c)
        n = len(s) // 2
        if s[:-n] == ''.join(reversed(s[n:])):
            b = str(bin(c))[2:]
            n = len(b) // 2
            if b[:-n] == ''.join(reversed(b[n:])):
                t += c
        c += 2
    return t


if __name__ == '__main__':
    print(double_base_palindromes())
