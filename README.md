Fun with math/computing problems from [Project Euler](https://projecteuler.net).

[![Build Status](https://travis-ci.org/lsbardel/mathfun.svg?branch=master)](https://travis-ci.org/lsbardel/mathfun)


Number theory
=============

* Prime numbers
* Greatest common divisor ``d = GCD(a, b)``
* ``GCD(a, b) = ua + vb``, unique ``u`` and ``v`` natural numbers
* If prime ``p`` divides the product ``ab``
```
ab // p == 0
then
a // p == 0 or b // p == 0
```
* If ``p`` does not divide ``a``, for statement above we have
```
ua + vp = 1
``` 
* If ``n`` is a natural number, than ``a`` and ``b`` are **congruent module n** if ``n`` divide their difference
```
if
n // (a-b) == 0
than
a % n == b % n 
```
we call this the ``[a]n`` the **congruent class module n containing a** with ``0 <= a < n-1``
