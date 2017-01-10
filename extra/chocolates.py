

def solution(N, M):
    # write your code in Python 2.7
    c = 1
    x = 0
    eaten = set((0,))
    while True:
        x = (x + M) % N
        if x in eaten:
            return c
        eaten.add(x)
        c += 1
    return c


def solution(N, M):
    # write your code in Python 2.7
    c = 1
    x = 0
    eaten = set((0,))
    while True:
        x = (x + M) % N
        if x in eaten:
            return c
        eaten.add(x)
        c += 1
    return c

if __name__ == '__main__':
    print(solution(10, 4))
