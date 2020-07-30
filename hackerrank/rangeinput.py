_input = list(
    reversed(
        """3
0 3
1 9
2 5
""".split(
            "\n"
        )
    )
)


def input():
    return _input.pop()


N = int(input().strip())
for _ in range(N):
    a, b = [int(v) for v in input().strip().split()]
