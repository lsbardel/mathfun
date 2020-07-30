from collections import Counter


def anagram1(s1, s2):
    if len(s1) == len(s2):
        return sorted(s1) == sorted(s2)
    return False


def anagram2(s1, s2):
    if len(s1) == len(s2):
        return Counter(s1) == Counter(s2)
    return False


def test_strings(size=500):
    import string
    from random import choice, shuffle
    letters = getattr(string, 'letters', getattr(string, 'ascii_letters', ''))
    all = [choice(letters) for c in range(size)]
    s1 = ''.join(all)
    shuffle(all)
    s2 = ''.join(all)
    return s1, s2


if __name__ == '__main__':
    import sys
    import timeit
    num = 100
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    print(timeit.timeit(
        'anagram1(s1, s2)',
        'from __main__ import test_strings, anagram1;'
        's1, s2 = test_strings(%s)' % num, number=1000)
    )
    print(timeit.timeit(
        'anagram2(s1, s2)',
        'from __main__ import test_strings, anagram2;'
        's1, s2 = test_strings(%s)' % num, number=1000)
    )
