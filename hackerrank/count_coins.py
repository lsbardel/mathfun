def coin_changes(coins, ammount):
    ways = [1] + [0] * ammount
    for c in sorted(coins):
        for j in range(c, ammount + 1):
            ways[j] += ways[j - c]
    return ways[ammount]


if __name__ == "__main__":
    print(coin_changes([2, 5, 3, 6], 10))
