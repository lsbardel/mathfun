# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Code Questions around the Web

# ## Buy low sell high
#
# Given an array of stock prices, minute by minute, write a function that return the best possible profit one could make from one buy and one sell. No shorting allowed, no buyng and selling at the same time.
#
# ### Solution
#
# This can be solved by keeping track of the lowest price at which we can by. The maximum profit will be given by the best difference with this.

import numpy as np

prices = np.random.randint(1, 40, 20)
prices

# +
from heapq import heappop, heappush


def buy_low_sell_high(P):
    buy = P[0]
    max_profit = None
    for p in P[1:]:
        profit = p - buy
        max_profit = profit if max_profit is None else max(max_profit, profit)
        buy = min(buy, p)
    return max_profit


# -

buy_low_sell_high(prices)

# ## Index Product
#
# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index. You cannot use division.

# ### Solution
#
# The fastest solution is to loop through the array twice, the first iteration calculate the product before each index, the second after.

import numpy as np

ints = np.random.randint(0, 10, 4)
ints


def index_product(A):
    P = []
    prod = 1
    for a in A:
        P.append(prod)
        prod *= a
    prod = 1
    N = len(A)
    for i, a in enumerate(reversed(A), 1):
        P[N-i] *= prod
        prod *= a
    return P


index_product(ints)
