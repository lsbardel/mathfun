

def count_summations(N):
    ways = [1] + [0]*N
    for n in range(1, N):
        for j in range(n, N+1):
            ways[j] += ways[j-n]
    # we don't consider the N alone, minumim two numbers
    return ways[N]


if __name__ == '__main__':
    print(count_summations(100))
