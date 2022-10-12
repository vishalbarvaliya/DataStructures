from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def bfs(self, source):
        visited = set()
        queue = deque()
        queue.append(source)
        visited.add(source)

        while queue:
            vertex = queue.popleft()  # Queue
            print(vertex, end=" ")
            for v in self.graph[vertex]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)


gra = Graph()
gra.addEdge(5, 7)
gra.addEdge(7, 6)
gra.addEdge(6, 5)
gra.addEdge(5, 6)
gra.addEdge(6, 7)
gra.bfs(5)
