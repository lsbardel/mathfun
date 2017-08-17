
_input = list(reversed("""40
...X......XX.X...........XX....X.XX.....
.X..............X...XX..X...X........X.X
......X....X....X.........X...........X.
.X.X.X..X........X.....X.X...X.....X..X.
....X.X.X...X..........X..........X.....
..X......X....X....X...X....X.X.X....XX.
...X....X.......X..XXX.......X.X.....X..
...X.X.........X.X....X...X.........X...
XXXX..X......X.XX......X.X......XX.X..XX
.X........X....X.X......X..X....XX....X.
...X.X..X.X.....X...X....X..X....X......
....XX.X.....X.XX.X...X.X.....X.X.......
.X.X.X..............X.....XX..X.........
..X...............X......X........XX...X
.X......X...X.XXXX.....XX...........X..X
...X....XX....X...XX.X..X..X..X.....X..X
...X...X.X.....X.....X.....XXXX.........
X.....XX..X.............X.XX.X.XXX......
.....X.X..X..........X.X..X...X.X......X
...X.....X..X.............X......X..X..X
........X.....................X....X.X..
..........X.....XXX...XX.X..............
........X..X..........X.XXXX..X.........
..X..X...X.......XX...X.....X...XXX..X..
.X.......X..............X....X...X....X.
.................X.....X......X.....X...
.......X.X.XX..X.XXX.X.....X..........X.
X..X......X..............X..X.X.......X.
X........X.....X.....X....XX.......XX...
X.....X.................X.....X..X...XXX
XXX..X..X.X.XX..X....X.....XXX..X......X
..........X.....X.....XX................
..X.........X..X.........X...X.....X....
.X.X....X...XX....X...............X.....
.X....X....XX.XX........X..X............
X...X.X................XX......X..X.....
..X.X.......X.X..X.....XX.........X..X..
........................X..X.XX..X......
........X..X.X.....X.....X......X.......
.X..X....X.X......XX....................
34 28 16 8
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


graph = Graph()

N = int(input().strip())
for i in range(N):
    for j, v in enumerate(input().strip()):
        if v == 'X':
            continue
        vertex = Vertex(i, j)
        graph.vertices[vertex.id] = vertex
        vid = (i - 1, j)
        while vid in graph.vertices:
            graph.add(vid, vertex.id)
            vid = vid[0] - 1, j
        vid = (i, j - 1)
        while vid in graph.vertices:
            graph.add(vid, vertex.id)
            vid = i, vid[1] - 1


last = tuple((int(v) for v in input().strip().split(' ')))

search = GraphSearch(graph, last[:2])
parents = search.bfs()
last = parents[last[2:]]
moves = 0
while last:
    moves += 1
    last = parents[last]

print(moves)
