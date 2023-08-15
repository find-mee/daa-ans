# TIME complexity: O(EV)
# SPACE complexity : O(V)

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []
        self.nodes = []

    def add_node(self,N):
        self.nodes.append(N)

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def printAns(self,dist):
        for key,value in dist.items() :
            print(f"{key}  {value}")
    
    def bellman(self,src):
        dist = {i : float("inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V-1):
            for u,v,w in self.graph:
                if dist[u]!=float('inf') and dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
                
        for u,v,w in self.graph:
                if dist[u]!=float('inf') and dist[u]+w < dist[v]:
                    print("Negative cycle exist")
                    return
                
        self.printAns(dist)


g = Graph(6)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_node("F")
g.add_edge("A", "B", -4)
g.add_edge("C", "B", 8)
g.add_edge("D", "A", 6)
g.add_edge("B", "D", -1)
g.add_edge("B", "E", -2)
g.add_edge("D", "F", 4)
g.add_edge("E", "F", 2)
g.add_edge("C", "F", 3)
g.add_edge("A", "F", -3)


src = "A"
g.bellman(src)



