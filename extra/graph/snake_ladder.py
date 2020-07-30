_input = list(
    reversed(
        """2
3
32 62
42 68
12 98
7
95 13
97 25
93 37
79 27
75 19
49 47
67 17
4
8 52
6 80
26 42
2 72
9
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
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
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def add(self, id1, id2):
        if id1 not in self.vertices:
            self.vertices[id1] = Vertex(id1)
        if id2 not in self.vertices:
            self.vertices[id2] = Vertex(id2)
        self.vertices[id1].links.add(self.vertices[id2].id)
        if not self.directed:
            self.vertices[id2].links.add(self.vertices[id1].id)


class GraphSearch:
    finished = False

    def __init__(self, graph, root):
        self.graph = graph
        self.root = root

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
        pass


T = int(input().strip())


for _ in range(T):
    graph = Graph(True)

    for _ in range(int(input().strip())):
        m, v = input().strip().split()
        graph.add(int(m), int(v))

    for _ in range(int(input().strip())):
        m, v = input().strip().split()
        graph.add(int(m), int(v))

    # add 1 and 100
    graph.vertices[1] = Vertex(1)
    graph.vertices[100] = Vertex(100)

    for i in range(1, 100):
        if graph.vertices[i].links:
            continue
        j = 0
        while j < 6 and i + j < 100:
            j += 1
            vertex = graph.vertices.get(i + j)
            if vertex and vertex.links:
                assert len(vertex.links) == 1
                graph.add(i, tuple(vertex.links)[0])
            else:
                graph.add(i, i + j)

    search = GraphSearch(graph, 1)
    parents = search.bfs()
    if 100 in parents:
        parent = parents[100]
        moves = 0
        while parent:
            parent = parents[parent]
            moves += 1
        print(moves)
    else:
        print(-1)
