from itertools import combinations


def count_money(start, money, idx=0, stop=200):
    count = 0
    size = money[idx]
    idx += 1
    for n in range(stop // size + 1):
        total = start + n*size
        if total >= stop:
            if total == stop:
                return count + 1
            break
        elif idx < len(money):
            count += count_money(total, money, idx, stop)
    return count



def problem31():
    return count_money(0, [100, 50, 20, 10, 5, 2, 1]) + 1



if __name__ == '__main__':
    print(problem31())
