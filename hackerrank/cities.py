_input = """8
16
4 5 0.35
4 7 0.37
5 7 0.28
0 7 0.16
1 5 0.32
0 4 0.38
2 3 0.17
1 7 0.19
0 2 0.26
1 2 0.36
1 3 0.29
2 7 0.34
6 2 0.40
3 6 0.52
6 0 0.58
6 4 0.93 """

_input = list(reversed(_input.split("\n")))


def input():
    return _input.pop()


from heapq import heappop, heappush

visited = {}


class Node:
    def __init__(self, number, neighbour):
        self.number = number
        self.neighbours = [neighbour]

    def __repr__(self):
        return "%d%s" % (self.number, self.neighbours)

    __str__ = __repr__

    def visit(self, node, skip=False):
        for n in self.neighbours:
            if node.number == n:
                return True
            if skip != n and visited[n].visit(node, self.number):
                return True
        return False


heap = []
N = int(input().strip())
M = int(input().strip())
for _ in range(M):
    a, b, d = input().strip().split()
    a, b, d = int(a), int(b), float(d)
    heappush(heap, (d, a, b))


total = 0

while len(visited) < N:
    include = False
    d, a, b = heappop(heap)

    if a not in visited:
        a = Node(a, b)
        visited[a.number] = a
        include = True

    if b not in visited:
        if not include:
            a = visited[a]
            a.neighbours.append(b)
        b = Node(b, a.number)
        visited[b.number] = b
        include = True
    elif include:
        b = visited[b]
        b.neighbours.append(a.number)

    if not include:
        a = visited[a]
        b = visited[b]
        aa = aa if len(a.neighbours) < len(b.neighbours) else b
        bb = b if aa is a else a
        if not aa.visit(bb):
            include = True
            a.neighbours.append(b.number)
            b.neighbours.append(a.number)

    if include:
        print("%s %s %s " % (a.number, b.number, d))
        total += d


print(total)
