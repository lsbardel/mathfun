from itertools import product


def problem209():
    vals = {}
    for i in product([0, 1], repeat=6):
        h = i[0] ^ (i[1] and i[2])
        j = i[1:] + (h,)
        if i in vals and j in vals:
            o1 = vals[i]
            o2 = vals[j]
            outcome = min(o1, o2)
            wrong = o1 + o2 - outcome
            for k, v in list(vals.items()):
                if v > wrong:
                    vals[k] = v - 1
                elif v == wrong:
                    vals[k] = outcome
        elif i in vals or j in vals:
            outcome = vals[i] if i in vals else vals[j]
        elif vals:
            outcome = max(vals.values()) + 1
        else:
            outcome = 1
        vals[i] = outcome
        vals[j] = outcome
    print(vals)


if __name__ == '__main__':
    problem209()
