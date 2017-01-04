

def pitogorean_triplet(T):
    b = T // 2 - 1
    T2 = T*T
    while b:
        a = (T2 - 2*T*b) // (2*(T - b))
        c = T - b - a
        if a*a + b*b == c*c:
            return a*b*c
        b -= 1


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 1000
    print(pitogorean_triplet(num))
