_input = list(
    reversed(
        """5 5 5
1 1
1 2
1 3
1 4
1 5
1 2 10
1 3 10
2 4 10
3 5 10
4 5 10
""".split(
            "\n"
        )
    )
)


def input():
    return _input.pop()


inf = float("infinity")


class Vertex:
    def __init__(self, id, score):
        self.id = id
        self.links = set()
        self.score = score

    def __repr__(self):
        return "%s %s" % (self.id, self.score)


class GraphSearch:
    """Search algorithms with callbacks
    """

    def __init__(self, g, root):
        self.graph = g
        self.finished = False
        self.root = root
        self.path = {root: None}
        self.visited = set()
        self.processed = set()
        self.time = 0

    def distance(self, vertex1, vertex2):
        if not vertex2.score:
            return inf
        return self.graph.distance(vertex1.id, vertex2.id)

    def process_vertex_early(self, vertex):
        vertex.score = None

    def process_vertex_late(self, vertex):
        pass

    def process_edge(self, parent, child):
        self.time += self.graph.distance(parent.id, child.id)


class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.roads = {}
        self.directed = directed

    def add(self, id1, id2, weight):
        if id1 not in self.vertices:
            self.vertices[id1] = Vertex(id1)
        if id2 not in self.vertices:
            self.vertices[id2] = Vertex(id2)
        self.vertices[id1].links.add(self.vertices[id2].id)
        if not self.directed:
            self.vertices[id2].links.add(self.vertices[id1].id)
        self.roads[self._rdid(id1, id2)] = weight

    def distance(self, id1, id2):
        return self.roads[self._rdid(id1, id2)]

    def _rdid(self, id1, id2):
        idm = min(id1, id2)
        return idm, id1 + id2 - idm

    def get_search(self, root, searchFactory=None):
        if not self.vertices:
            raise ValueError("No vertices")
        if not isinstance(root, Vertex):
            root = self.vertices[root]
        search = (searchFactory or GraphSearch)(self, root)
        return search

    def shortest_path(self, start, end, search=None):
        search = self.get_search(start)

        vertex = search.root
        end = self.vertices[end]

        while vertex != end:
            if search.finished:
                break

            search.process_vertex_early(vertex)

            vnext = None
            current_weight = inf

            for idv in vertex.links:
                adj = self.vertices[idv]
                if adj in search.path:
                    continue
                weight = search.distance(vertex, adj)
                if vnext is None or weight < current_weight:
                    current_weight = weight
                    vnext = adj

            if not vnext:
                return search

            search.process_edge(vertex, vnext)
            search.path[vnext] = vertex
            search.process_vertex_late(vertex)
            vertex = vnext

        search.process_vertex_early(vertex)
        search.process_vertex_late(vertex)

        return search


graph = Graph()

N, M, K = [int(v) for v in input().strip().split()]

for i in range(N):
    T = [int(v) for v in input().strip().split()]
    graph.vertices[i + 1] = Vertex(i + 1, T[1:])

for m in range(M):
    i1, i2, weight = [int(v) for v in input().strip().split()]
    graph.add(i1, i2, weight)


search1 = graph.shortest_path(1, N)
search2 = graph.shortest_path(1, N)

print(max(search1.time, search2.time))
