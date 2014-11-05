import sys
if sys.version_info[0] == 2:
    from itertools import izip as zip


def triangle_path(triangle):
    summation = triangle[-1]
    for row in reversed(triangle[:-1]):
        new_summation = []
        for v, v1, v2 in zip(row, summation, summation[1:]):
            new_summation.append(v + max(v1, v2))
        summation = new_summation
    return summation[0]


test = '''\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def read_data():
    if len(sys.argv) > 1 and sys.argv[1] == '18':
        text = test
    else:
        import requests
        text = requests.get('https://projecteuler.net/project/resources/p067_triangle.txt').text
    return [[int(v) for v in line.split(' ')] for line in text.split('\n') if line]


if __name__ == '__main__':
    import timeit
    t = timeit.timeit('triangle_path(triangle)','''\
from __main__ import triangle_path, read_data
triangle = read_data()''', number=10)
    print(t)
    print(triangle_path(read_data()))