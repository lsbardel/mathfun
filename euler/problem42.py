"""https://projecteuler.net/problem=42
"""
from functools import reduce
from math import ceil, sqrt
from string import ascii_letters

positions = dict(((l, p) for p, l in enumerate(ascii_letters, 1)))


def problem42(names):
    cache = set()
    total = 0
    for name in names:
        tnum = reduce(lambda x, y: x + positions[y], name, 0)
        if tnum in cache:
            total += 1
        else:
            num = ceil(sqrt(tnum))
            t = num*(num+1)//2
            cache.add(t)
            while t < tnum:
                num += 1
                t = num*(num+1)//2
                cache.add(t)
            if t == tnum:
                total += 1
    return total


if __name__ == '__main__':
    import requests
    text = requests.get(
        'https://projecteuler.net/project/resources/p042_words.txt'
    ).text
    names = [n[1:-1].lower() for n in text.split(',') if n]
    print(problem42(names))
