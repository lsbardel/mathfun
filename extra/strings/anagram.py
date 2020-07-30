from collections import Counter
from itertools import combinations


def anagram(s):
    """find the minimum number of characters of the first string to
    change so it becomes an anagram of the second string.
    """
    n = len(s)
    tot = -1
    if n and not (n % 2):
        n //= 2
        tot = n
        s2 = iter(sorted(s[n:]))
        c2 = next(s2)
        for c1 in sorted(s[:n]):
            while c2 <= c1:
                found = c1 == c2
                tot -= found
                try:
                    c2 = next(s2)
                except StopIteration:
                    return tot
                if found:
                    break
    return tot


def anagram2(s1, s2):
    """Given two strings, that may or may not be of the same length,
    determine the minimum number of character deletions required to make
    them anagrams. Any characters can be deleted from either of the strings.
    """
    s1 = Counter(s1)
    s2 = Counter(s2)
    tot = 0
    for c, n in s1.items():
        tot += abs(n - s2.pop(c, 0))
    for n in s2.values():
        tot += n
    return n


def anagrammatic_pairs(s):
    N = len(s)
    tot = 0
    for n in range(N - 1):
        for a, b in combinations(
            ("".join(sorted(s[i : i + n + 1])) for i in range(N - n)), 2
        ):
            tot += a == b
    return tot


def palindrome_anagram(S):
    """Find an anagram of the string that is palindrome
    """
    visited = set()
    for s in S:
        if s in visited:
            visited.remove(s)
        else:
            visited.add(s)
    return len(visited) <= 1


if __name__ == "__main__":
    print(palindrome_anagram("cdefghmnopqrstuvw"))
