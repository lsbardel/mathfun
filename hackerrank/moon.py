
_input = list(reversed("""100000 2
1 2
3 4
""".split('\n')))


def input():
    return _input.pop()


from collections import deque


class Vertex:
    def __init__(self, id, score=1):
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
                for vid in vertex.links:
                    adj = self.graph.vertices[vid]
                    if adj not in processed:
                        if adj not in visited:
                            visited.add(adj)
                            queue.appendleft(adj)
                            self.parents[adj.id] = vertex.id

        return self.parents


graph = Graph()

N, I = [int(v) for v in input().strip().split()]
for _ in range(I):
    a, b = [int(v) for v in input().strip().split()]
    graph.add(a, b)

processed = set()
countries = []
rest = [a]
total = 0

while rest:
    country = set(GraphSearch(graph, rest[0]).bfs())
    countries.append(country)
    processed.update(country)
    rest = tuple(set(graph.vertices) - processed)

for i, country in enumerate(countries, 1):
    total += len(country) * (N - len(processed))
    for other in countries[i:]:
        total += len(country) * len(other)

print(total)
