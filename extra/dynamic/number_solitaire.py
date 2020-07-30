def solution(A):
    i = 1
    N = len(A)
    assert N > 1, N
    score = A[0] + A[N - 1]
    moves = [0]
    while i < len(A) - 6:
        this_score = None
        this_moves = []
        for j, a in enumerate(A[i : i + 6], i):
            if this_score is None:
                this_score = a
                i = j + 1
            elif this_score + a >= this_score:
                this_score = max(this_score, 0) + a
                this_moves.append(j)
                i = j + 1
        if not this_moves:
            this_moves.append(i - 1)
        moves.extend(this_moves)
        score += this_moves
    while i < N - 1:
        if A[i] > 0:
            moves.append(i)
            score += A[i]
        i += 1
    return score


if __name__ == "__main__":
    print(solution([1, -2, 3, 8, -4, -2, -1, -2, -4, -1, 6]))
