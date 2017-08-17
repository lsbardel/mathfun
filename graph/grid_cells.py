

_input = list(reversed("""5
5
1 1 0 0 0
0 1 1 0 0
0 0 1 0 1
1 0 0 0 1
0 1 0 1 1
""".split('\n')))


def input():
    return _input.pop()

from collections import deque


class Vertex:
    def __init__(self, i, j):
        self.id = (i, j)
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


class GraphSearch:
    finished = False

    def __init__(self, graph, toprocess):
        self.graph = graph
        self.toprocess = toprocess
        self.root = toprocess.pop()

    def bfs(self):
        visited = set()
        processed = set()
        queue = deque()

        self.parents = {}

        if not graph.vertices:
            return

        vertex = self.graph.vertices[self.root or 0]
        self.parents[vertex.id] = None

        queue.append(vertex)

        while queue:
            if self.finished:
                break

            vertex = queue.pop()
            if vertex not in processed:
                processed.add(vertex)
                self.vertex_processed(vertex)
                for vid in vertex.links:
                    adj = self.graph.vertices[vid]
                    if adj not in processed:
                        if adj not in visited:
                            visited.add(adj)
                            queue.appendleft(adj)
                            self.parents[adj.id] = vertex.id

        return self.parents

    def vertex_processed(self, vertex):
        self.toprocess.discard(vertex.id)


N = int(input().strip())
M = int(input().strip())
NM = N*M

graph = Graph(N)
filled = {}

for n in range(N):
    for m, v in enumerate(input().strip().split()):
        if v == '1':
            vertex = Vertex(n + 1, m + 1)
            graph.vertices[vertex.id] = vertex

for vertex in graph.vertices.values():
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            vid = (vertex.id[0] + i, vertex.id[1] + j)
            if vid != vertex.id and 0 < vid[0] <= N and 0 < vid[1] <= M:
                other = graph.vertices.get(vid)
                if other:
                    vertex.links.add(other.id)
                    other.links.add(vertex.id)

toprocess = set(graph.vertices)
T = 0
while toprocess:
    search = GraphSearch(graph, toprocess)
    parents = search.bfs()
    T = max(T, len(parents))

print(T)
