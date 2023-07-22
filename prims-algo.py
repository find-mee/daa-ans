import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        print(self.graph)
    def add_edge(self, u, v, cost):
        self.graph[u][v] = cost
        self.graph[v][u] = cost
        print(self.graph)

    def find_min_cost(self):
        min_cost = [sys.maxsize] * self.V
        min_cost[0] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            min_vertex = self.find_min_vertex(min_cost, visited)
            visited[min_vertex] = True

            for v in range(self.V):
                if self.graph[min_vertex][v] > 0 and not visited[v] and self.graph[min_vertex][v] < min_cost[v]:
                    min_cost[v] = self.graph[min_vertex][v]

        return sum(min_cost)

    def find_min_vertex(self, min_cost, visited):
        min_value = sys.maxsize
        min_vertex = -1

        for v in range(self.V):
            if not visited[v] and min_cost[v] < min_value:
                min_value = min_cost[v]
                min_vertex = v

        return min_vertex


# Input graph
g = Graph(7)
g.add_edge(0, 1, 4)
g.add_edge(0, 3, 8)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 1)
g.add_edge(3, 2, 7)
g.add_edge(3, 5, 3)
g.add_edge(4, 5, 6)
g.add_edge(4, 6, 3)
g.add_edge(5, 6, 8)

min_cost = g.find_min_cost()
print("Minimum cost:", min_cost)
