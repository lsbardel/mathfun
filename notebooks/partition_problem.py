# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from functools import lru_cache
from typing import Sequence

import numpy as np


def partition_problem(S: Sequence[int], K: int):
    """B is a sequence of positive integers while K is the number of partitions.

    Problem: Integer Partition without Rearrangement
    Output: Partition S into K < len(S) to minimize the maximum sum over all ranges,
    without reordering S.
    """
    assert K > 0, K
    
    N = len(S)
    c = np.cumsum(S)
    p = np.zeros((N, K), dtype=int)
    m = np.zeros((N, K), dtype=int)
    #
    # Initialize boundaries for the cost matrix
    # the smallest possible first partitions is given by first element
    m[0, :] = S[0]
    # when K is 1 we don't partition at all
    m[:, 0] = c
    maxv = m[N-1, 0]
    #
    # evaluate the cost matrix
    for i in range(1, N):
        for k in range(1, K):
            m[i, k] = maxv
            for j in range(i):
                cost = max(m[j,k-1], c[i]-c[j])
                if m[i, k] > cost:
                    m[i, k] = cost
                    p[i, k] = j+1
    p = list(p[N-1, :])
    p.append(N-1)
    splits = []
    for i1, i2 in zip(p[:-1], p[1:]):
        splits.append(S[i1:i2])
    
    return m, splits, p



# %%
S = np.random.randint(1, 2, (9,))
S = np.arange(1, 10)
S

# %%
m, p, splits = partition_problem(S, 3)
m, p, splits

# %%
S[3:5]

# %%
