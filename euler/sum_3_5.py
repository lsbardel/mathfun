
def multiple_sum():
    all = set((5*i for i in range(200)))
    all.update((3*i for i in range(334)))
    return sum(all)


def multiple_sum2(number):
    num = lambda x, y : x + y if (y % 3 == 0 or y % 5 == 0) else x
    return reduce(num, range(number))


if __name__ == '__main__':
    print(multiple_sum2(1000))
