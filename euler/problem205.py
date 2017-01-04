

def dice(faces=6, total=1):
    prob = {0: 1}
    m = 1./faces
    for _ in range(total):
        prev = prob
        prob = {}
        for c, p in prev.items():
            for f in range(1, faces+1):
                f += c
                value = prob.get(f, 0)
                prob[f] = value + p*m
    return prob


def problem205():
    d4 = dice(4, 9)
    d6 = dice(6, 6)
    print(sum(d4.values()))
    print(sum(d6.values()))
    start = min(min(d4), min(d6))
    end = max(max(d4), max(d6))
    p = 0
    k = 1
    for k in range(1, end):
        for i in range(start, end+1):
            f4 = d4.get(i, 0)
            f6 = d6.get(i-k, 0)
            p += f4*f6
    return p


if __name__ == '__main__':
    print('%.7f' % problem205())
