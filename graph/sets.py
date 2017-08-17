from collections import deque


class Vertex:
    def __init__(self, id):
        self.id = id
        self.links = set()


class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def add(self, id1, id2):
        if id1 not in self.vertices:
            self.vertices[id1] = Vertex(id1)
        if id2 not in self.vertices:
            self.vertices[id2] = Vertex(id2)
        self.vertices[id1].links.add(self.vertices[id2].id)
        self.vertices[id2].links.add(self.vertices[id1].id)

    def bfs(self, root):
        visited = set()
        queue = deque()
        parents = {}

        if not graph.vertices:
            return

        vertex = self.vertices[root or 0]
        parents[vertex.id] = None

        queue.append(vertex)

        while queue:
            vertex = queue.pop()
            visited.add(vertex)
            for vid in vertex.links:
                adj = self.vertices[vid]
                if adj not in visited:
                    visited.add(adj)
                    queue.appendleft(adj)
                    parents[adj.id] = vertex.id

        return parents



_input = list(reversed("""5
1 6
2 7
3 8
4 9
2 6
""".split('\n')))


def input():
    return _input.pop()


import sys

graph = Graph()


for _ in range(int(input().strip())):
    a, b = [int(v) for v in input().strip().split()]
    graph.add(a, b)

toprocess = set(graph.vertices)
mins = sys.maxsize
maxs = 0

while toprocess:
    parents = graph.bfs(toprocess.pop())
    N = len(parents)
    mins = min(mins, N)
    maxs = max(maxs, N)
    toprocess.difference_update(parents)

print('%d %d' % (mins, maxs))
