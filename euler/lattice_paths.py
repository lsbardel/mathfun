

def count_paths(i, j, cache):
    if i*j:
        if (i, j) in cache:
            return cache[(i, j)]
        else:
            count = count_paths(i-1, j, cache) + count_paths(i, j-1, cache)
            cache[(i, j)] = count
            return count
    else:
        return 1


def lattice_paths(num):
    cache = {}
    return count_paths(num, num, cache)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 20
    print(lattice_paths(num))