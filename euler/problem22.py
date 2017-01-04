"""https://projecteuler.net/problem=22
"""
from string import ascii_letters

import requests


def problem22():
    text = requests.get(
        'https://projecteuler.net/project/resources/p022_names.txt'
    ).text
    names = [t[1:-1].lower() for t in text.split(',') if t]
    scores = dict(((letter, pos) for pos, letter
                   in enumerate(ascii_letters, 1)))
    total = 0
    for n, name in enumerate(sorted(names), 1):
        total += n*sum((scores[c] for c in name))
    return total


if __name__ == '__main__':
    print(problem22())
