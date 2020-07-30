"""https://projecteuler.net/problem=54
"""
from collections import Counter
from enum import Enum

import requests

numbers = dict(((str(v), v) for v in range(2, 10)))
numbers.update(dict(T=10, J=11, Q=12, K=13, A=14))


class Pocker(Enum):
    no_hand = -1
    high_card = 0
    pair = 1
    two_pairs = 2
    three_of_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_kind = 7
    stright_flush = 8


class hand:

    def __init__(self, cards):
        counter = Counter()
        suits = set()
        for c in cards:
            number = numbers[c[0]]
            suits.add(c[1])
            counter[number] += 1

        N = len(counter)
        self.cards = sorted(counter)
        self.rank = Pocker.no_hand
        if N == 5:
            high = 0
            for card in self.cards:
                if high and card != high+1:
                    self.rank = Pocker.high_card
                    break
                high = card
            if self.rank == Pocker.no_hand:
                self.rank = (
                    Pocker.straight if len(suits) > 1 else Pocker.stright_flush
                )
        elif len(suits) == 1:
            self.rank = Pocker.flush
        else:
            pair = None
            for card, count in counter.items():
                if count == 4:
                    self.rank = Pocker.four_of_kind
                elif count == 3:
                    self.rank = (
                        Pocker.full_house if N == 2 else Pocker.three_of_kind
                    )
                elif count == 2 and N == 4:
                    self.rank = Pocker.pair
                elif count == 2 and N == 3:
                    if not pair:
                        pair = card
                    else:
                        self.rank = Pocker.two_pairs
                        c = min(card, pair)
                        self.cards.remove(c)
                        self.cards.append(c)
                        card = max(card, pair)

                if self.rank != Pocker.no_hand:
                    self.cards.remove(card)
                    self.cards.append(card)
                    break
        if self.rank == Pocker.no_hand:
            raise ValueError('%s' % self)

    def __repr__(self):
        return '%s: %s' % (self.rank, self.cards)
    __str__ = __repr__

    def __gt__(self, other):
        if self.rank == other.rank:
            for c1, c2 in zip(reversed(self.cards), reversed(other.cards)):
                if c1 == c2:
                    continue
                return c1 > c2
        return self.rank.value > other.rank.value


def poker_hands(text):
    count = 0
    for line in text.split('\n'):
        if line:
            cards = line.split()
            one = hand(cards[:5])
            two = hand(cards[5:])
            count += one > two

    return count


if __name__ == '__main__':
    import time
    text = requests.get(
        'https://projecteuler.net/project/resources/p054_poker.txt'
    ).text
    start = time.monotonic()
    result = poker_hands(text)
    print('time: %.4f, result: %d' % (time.monotonic() - start, result))
