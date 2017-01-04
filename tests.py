import unittest

from mathfun.prime_numbers import prime_factors, factors


def pf(n):
    return sorted(prime_factors(n))


def fs(n, cache=None):
    return sorted(factors(n, cache))


class TestMath(unittest.TestCase):

    def test_prime_factors(self):
        self.assertEqual(pf(2), [2])
        self.assertEqual(pf(3), [3])
        self.assertEqual(pf(4), [2, 2])
        self.assertEqual(pf(5), [5])
        self.assertEqual(pf(6), [2, 3])
        self.assertEqual(pf(7), [7])
        self.assertEqual(pf(8), [2, 2, 2])
        self.assertEqual(pf(18), [2, 3, 3])
        self.assertEqual(pf(20), [2, 2, 5])

    def test_prime_factors_cache(self):
        cache = {}
        cache[20] = prime_factors(20, cache)
        self.assertEqual(len(cache), 2)
        self.assertEqual(cache[5], [5])

    def test_factors(self):
        self.assertEqual(fs(20), [1, 2, 4, 5, 10])
        self.assertEqual(fs(220), [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
        self.assertEqual(fs(1210),
                         [1, 2, 5, 10, 11, 22, 55, 110, 121, 242, 605])

    def test_factor_cache(self):
        cache = {}
        for n in range(1000, 1, -1):
            factors(n, cache)
        self.assertEqual(fs(220, cache),
                         [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])


if __name__ == '__main__':
    unittest.main()
