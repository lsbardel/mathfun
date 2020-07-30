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
    p = np.zeros((N + 1,), dtype=int)
    m = np.zeros((N + 1, K + 1), dtype=int)
    # the smallest possible first partitions is given by first element
    m[1, :] = S[0]
    m[:, 1] = p
    np.cumsum(S, out=p[1:])
    # initialize boundaries
    print(p)


if __name__ == "__main__":
    S = np.random.randint(1, 5, (20,))
    partition_problem(S, 4)
