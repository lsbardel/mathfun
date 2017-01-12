
def count(V):
    V = sorted([int(v) for v in V.split()])
    base = V[0]
    tot = 0
    for i, v in enumerate(V[1:], 1):
        v -= base
        steps = v // 5
        tot += steps
        V[i] -= 5*steps
        d = v % 5
    return tot


def add(N, step, V, i):
    s = N // step
    if s:
        V[i] -= s*step
        return s


if __name__ == '__main__':
    print(count('2 2 3 7'))
    print(count('53 361 188 665 786 898 447 562 272 123 229 629 670 848 994 54 822 46 208 17 449 302 466 832 931 778 156 39 31 777 749 436 138 289 453 276 539 901 839 811 24 420 440 46 269 786 101 443 832 661 460 281 964 278 465 247 408 622 638 440 751 739 876 889 380 330 517 919 583 356 83 959 129 875 5 750 662 106 193 494 120 653 128 84 283 593 683 44 567 321 484 318 412 712 559 792 394 77 711 977 785 146 936 914 22 942 664 36 400 857'))


def console():
    t = int(input().strip())
    for _ in range(t):
        S = input().strip()
        print(lexo(S))
