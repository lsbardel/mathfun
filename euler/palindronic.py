

def palindromic(digits):
    lower = 10**(digits-1)
    d1 = 10*lower-1
    mp = 0
    while d1 >= lower:
        d2 = d1
        while d2 >= lower:
            p = d1*d2
            if p < mp:
                break
            ps = str(p)
            if ps == ps[::-1]:  # check palindromic
                mp = p
                break
            d2 -= 1
        d1 -= 1
    return mp


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 3
    print(palindromic(num))
