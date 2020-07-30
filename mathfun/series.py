def fibonacci():
    """generartor of fibonacci numbers"""
    a, b, n = 0, 1, 1
    yield n, b
    while True:
        n += 1
        a, b = b, b + a
        yield n, b


def triangle():
    n = 1
    while True:
        yield n, n * (n + 1) // 2
        n += 1
