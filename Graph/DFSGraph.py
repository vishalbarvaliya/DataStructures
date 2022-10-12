from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def dfs(self, source):
        visited = set()
        queue = deque()
        queue.append(source)
        visited.add(source)

        while queue:
            vertex = queue.pop()  # Stack
            print(vertex, end=" ")
            for v in self.graph[vertex]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)


gra = Graph()
gra.addEdge(0, 1)
gra.addEdge(0, 2)
gra.addEdge(1, 0)
gra.addEdge(1, 3)
gra.addEdge(1, 4)
gra.addEdge(2, 0)
gra.addEdge(3, 1)
gra.addEdge(4, 2)
gra.addEdge(4, 3)
gra.dfs(0)
