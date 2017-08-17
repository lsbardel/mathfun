from collections import deque


class Vertex:
    def __init__(self, id):
        self.id = id
        self.links = set()


class GraphSearch:
    """Search algorithms with callbacks
    """
    def __init__(self, g, root):
        self.graph = g
        self.finished = False
        self.root = root
        self.parents = {root.id: None}
        self.visited = set()
        self.processed = set()

    def process_vertex_early(self, vertex):
        pass

    def process_vertex_late(self, vertex):
        pass

    def process_edge(self, parent, child):
        pass


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

    def get_search(self, root, searchFactory=None):
        if not self.vertices:
            raise ValueError('No vertices')
        if not isinstance(root, Vertex):
            root = self.vertices[root]
        search = (searchFactory or GraphSearch)(self, root)
        return search

    def bfs(self, root, searchFactory=None):
        search = self.get_search(root, searchFactory)
        queue = deque()
        queue.append(search.root)

        while queue:
            if search.finished:
                break

            vertex = queue.pop()
            if vertex not in search.processed:
                search.process_vertex_early(vertex)
                search.processed.add(vertex)
                for vid in vertex.links():
                    adj = self.vertices[vid]

                    if adj in search.processed:
                        if self.directed:
                            search.process_edge(vertex, adj)
                    else:
                        search.process_edge(vertex, adj)

                        if adj not in search.visited:
                            search.visited.add(adj)
                            queue.appendleft(adj)
                            search.parents[adj.id] = vertex.id

                search.process_vertex_late(vertex)

        return search

        return self.parents
