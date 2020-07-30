def pairs(a, k):
    count = 0
    for i, ai in enumerate(a[:-1], 1):
        for aj in a[i:]:
            if not (ai + aj) % k:
                count += 1
    return count


def bitwise_and(n, k):
    k1 = k - 1


if __name__ == "__main__":
    print(pairs([1, 3, 2, 6, 1, 2], 3))
