def solution(A):
    unique = set()
    for a in A:
        if a in unique:
            unique.remove(a)
        else:
            unique.add(a)
    return unique.pop()
