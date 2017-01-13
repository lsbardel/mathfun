Fun with math/computing problems from [Project Euler](https://projecteuler.net).

[![Build Status](https://travis-ci.org/lsbardel/mathfun.svg?branch=master)](https://travis-ci.org/lsbardel/mathfun)



# Prime numbers

Greatest common divisor ``d = GCD(a, b)``

## Extended Euclidean Algorithm

The [extended GCD algorithm](https://github.com/lsbardel/mathfun/blob/master/mathfun/primes/gcd.py#L18) states that,
for two natural numbers ``a`` and ``b``
```
GCD(a, b) = ua + vb
```
with ``u`` and ``v`` unique natural numbers.
Because ``u a % a == 0`` and ``v b % b == 0`` we can expresse the theorem as
```
vb % a == 1 % a
ua % b == 1 % b
```

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

If a prime number ``p`` does not divide ``a``, in other words ``a`` is in ``[n]p`` with ``n != 0``, thanks to the extended gcd we have
```
ua + vp = 1
```
If ``p`` is prime, than for any natural number ``n``
```
(n^p - n) % p == 0
```
In other words, ``n^p`` and ``n`` are congruent module ``p`` for any prime number.

## Chinese Reminder Theorem

Let ``a`` and ``b`` be natural numbers with ``gcd(a, b) = 1``, and let ``c`` and ``d`` be arbitrary integers. Then there is a solution to the simultaneous congruences
```
(x - c) % a == 0
(x - d) % b == 0
```
Moreover, the solution is unique modulo ``ab``; that is, if ``x1`` and ``x2`` are two solutions,
then ``(x1 - x2) % ab == 0``.

**Fore example**: find an explicit formula for the solution to the two simultaneous congruences
```
x ≡ a % 131,
x ≡ b % 52
```
we use the extended GCD to find
```
xgcd(131, 52) = 1, -25, 63
```
which means
```
63*52 ≡ 1 % 131
-25*131 ≡ 1 % 52
```
and
```
x = 63*52 a - 25*13 b
```
