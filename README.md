Fun with math/computing problems from [Project Euler](https://projecteuler.net).

[![Build Status](https://travis-ci.org/lsbardel/mathfun.svg?branch=master)](https://travis-ci.org/lsbardel/mathfun)



# Prime numbers

Greatest common divisor ``d = GCD(a, b)``
``GCD(a, b) = ua + vb``, unique ``u`` and ``v`` natural numbers
If prime ``p`` divides the product ``ab``
```
ab // p == 0
then
a // p == 0 or b // p == 0
```
## Euclidean Algorithm

If ``p`` does not divide ``a``, for statement above we have
```
ua + vp = 1
``` 
for ``u`` and ``v`` unique natural numbers

## Congruent numbers

If ``n`` is a natural number, than ``a`` and ``b`` are **congruent module n** if ``n`` divide their difference
```
if
n // (a-b) == 0
than
a % n == b % n 
```
we call this the ``[a]n`` the **congruent class module n containing a** with ``0 <= a < n-1``. This class contains all the natural numbers for which their reminder with ``n`` is ``a``
For example the congruent class module 8 containing 5, [5]8 has the following numbers
```
[..., -11, -3, 5, 13, 21, 29, ...]
```
and
```
[3]4 = [..., -1, 3, 7, 11, ...]
```
```
[0]7 = [..., -7, 0, 7, 14, ...[
```
## Fermat Little Theorem

If ``p`` is prime, than for any natural number ``n``
```
(n^p - n) % p == 0
```
In other words, ``n^p`` and ``n`` are congruent module ``p`` for any prime number.
