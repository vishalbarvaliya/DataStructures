from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def __str__(self):
        data = []
        for i, j in self.graph.items():
            data.append(str([i, j]))
        return '\n'.join(data)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def getVertices(self):
        return list(self.graph.keys())

    def getEdges(self):
        edges = []
        for key in self.graph:
            for value in self.graph[key]:
                edges.append((key, value))
        return edges

    def getEdgesOf(self, vertex):
        if vertex in self.graph.keys():
            return self.graph[vertex]


gra = Graph()
gra.addEdge(5, 7)
gra.addEdge(7, 6)
gra.addEdge(6, 5)
gra.addEdge(5, 6)
gra.addEdge(6, 7)
print(gra.graph)
