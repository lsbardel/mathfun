_input = list(
    reversed(
        """2
4 2
1 2
1 3
1
3 1
2 3
2
""".split(
            "\n"
        )
    )
)


def input():
    return _input.pop()


from collections import deque


class Vertex:
    def __init__(self, id):
        self.id = id
        self.links = set()


class Graph:
    def __init__(self, N, directed=False):
        self.vertices = dict(((n, Vertex(n)) for n in range(1, N + 1)))
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

    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.result = dict(((vid, -1) for vid in self.graph.vertices))

    def bfs(self):
        visited = set()
        processed = set()
        queue = deque()

        self.parents = {}

        if not graph.vertices:
            return

        vertex = self.graph.vertices[self.root or 0]
        self.parents[vertex.id] = None
        self.result[vertex.id] = 0

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
        pid = self.parents[vertex.id]
        if pid is not None:
            self.result[vertex.id] = self.result[pid] + 6


Q = int(input().strip())

for q in range(Q):
    N, M = [int(v) for v in input().strip().split()]
    graph = Graph(N)

    for _ in range(M):
        a, b = [int(v) for v in input().strip().split()]
        graph.add(a, b)

    search = GraphSearch(graph, int(input().strip()))
    search.bfs()
    search.result.pop(search.root)
    print(" ".join((str(search.result[vid]) for vid in sorted(search.result))))
