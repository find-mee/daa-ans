class Union:
    def __init__(self, vertices):
        self.parent = [i for i in range(vertices)]

    def find(self,x):
        if self.parent[x] ==x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u,v):
        parent_x = self.find(u)
        parent_y = self.find(v)
        self.parent[parent_x] = parent_y

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, cost):
        self.edges.append((u,v,cost))

    def kruskal(self):
        self.edges.sort(key = lambda x:x[2])
        minimum_spanning_graph = []
        total_cost =0
        union_find = Union(self.vertices)

        for edge in self.edges:
            u,v,cost = edge
            if union_find.find(u) != union_find.find(v):
                union_find.union(u,v)
                minimum_spanning_graph.append(edge)
                total_cost += cost

        return minimum_spanning_graph, total_cost

connections = [
    [1, 5, 5],
    [1, 2, 10],
    [2, 3, 1],
    [2, 4, 6],
    [5, 4, 3],
    [5, 3, 7],
    [4, 3, 2]
]

vertices = 5

graph = Graph(vertices)

for edge in connections:
    u,v,cost = edge
    graph.add_edge(u-1,v-1,cost)

minimum_spanning_graph, total_cost = graph.kruskal()

print("minimun spanning tree:")
for edge in minimum_spanning_graph:
    u,v,cost = edge
    print(f"{u+1} to {v+1} is {cost}")

print(f"total cost {total_cost}")