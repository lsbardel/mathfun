from collections import deque


class Vertex:
    def __init__(self, id, score=1):
        self.id = id
        self.links = set()
        self.score = score


class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def extend_edges(self, edges):

        for edge in edges:
            id1 = edge[0]
            id2 = edge[1]
            if id1 not in self.vertices:
                self.vertices[id1] = Vertex(id1)
            if id2 not in self.vertices:
                self.vertices[id2] = Vertex(id2)
            self.vertices[id1].add_link(self.vertices[id2].id)
            if not self.directed:
                self.vertices[id2].add_link(self.vertices[id1].id)


class GraphSearch:
    finished = False

    def bfs(self, graph):
        """Breadth-first search algorithm
        """
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
                self.process_vertex_early(vertex)
                processed.add(vertex)
                for vid in vertex.links():
                    adj = self.graph.vertices[vid]

                    if adj in processed:
                        if self.graph.directed:
                            self.process_edge(vertex, adj)
                    else:
                        self.process_edge(vertex, adj)

                        if adj not in visited:
                            visited.add(adj)
                            queue.appendleft(adj)
                            self.parents[adj.id] = vertex.id

                self.process_vertex_late(vertex)

        return self.parents
