from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSort(self):
        visited = set()
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.__topologicalSortUtil(k, visited, stack)

        print(stack[::-1])

    def __topologicalSortUtil(self, v, visited, stack):
        visited.add(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        stack.append(v)


g = Graph()
g.addEdge(0, 2)
g.addEdge(2, 4)
g.addEdge(4, 7)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(1, 3)
g.addEdge(1, 2)
g.addEdge(3, 5)
g.topologicalSort()
