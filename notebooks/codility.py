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
def solution(A):
    c = 0
    vals = set()
    for a in A:
        a = abs(a)
        if a not in vals:
            vals.add(a)
    return len(vals)


# %%
A=[-5,-3,-1,0,3,6]
solution(A)


# %% [markdown]
# ## CountDistinctSlides
#
# This does not score that well (40%), caterpillar method

# %%
def solution(M, A):
    cmax = 1000000000
    s = set()
    count = 0
    for a in A:
        if a in s:
            count += len(s) * (len(s) + 1) // 2
            if count >= cmax:
                return cmax
            s = set()
        s.add(a)
    count += len(s) * (len(s) + 1) // 2
    return min(cmax, count)


# %%
solution(6, [3, 4, 5, 5, 2])

# %% [markdown]
# ## MinAbsSumOfTwo
#
# Caterpillar method (100% score)

# %%
import sys


def solution(A):
    mv = sys.maxsize
    B = sorted(set(A))
    h = 0
    t = len(B) - 1
    mv = abs(B[h] + B[t])
    while h <= t:
        v = B[h] + B[t]
        mv = min(mv, abs(v))
        if mv == 0:
            return mv
        if v > 0:
            t -= 1
        else:
            h += 1
    return mv
            


# %%
solution([-8, 4, 5, -10, 3])


# %% [markdown]
# ## NumberSolitaire
#
# Dynamic programming

# %%
def solution(A):
    i = 1
    score = A[0]
    moves = [0]
    while i < len(A) - 6:
        for j, a in enumerate(A[i : i + 6], i):
            if score + a >= score:
                score += a
                moves.append(j)
                i = j + 1
    while i < len(A):
        if A[i] > 0:
            moves.append(i)
            score += A[i]
        i += 1
    return score


# %%
solution([1, -2, 0, 9, -1, -2])

# %%
