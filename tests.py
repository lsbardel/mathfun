import unittest

from mathfun.prime_numbers import prime_factors, factors


class TestMath(unittest.TestCase):

    def test_prime_factors(self):
        pf = lambda n: sorted(prime_factors(n))
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
        fs = lambda n: sorted(factors(n))
        self.assertEqual(fs(20), [1, 2, 4, 5, 10])
        self.assertEqual(fs(220), [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
        self.assertEqual(fs(1210),
                         [1, 2, 5, 10, 11, 22, 55, 110, 121, 242, 605])

    def test_factor_cache(self):
        fs = lambda n, cache: sorted(factors(n, cache))
        cache = {}
        for n in range(1000, 1, -1):
            factors(n, cache)
        self.assertEqual(fs(220, cache),
                         [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])



if __name__ == '__main__':
    unittest.main()
