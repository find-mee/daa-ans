import sys

def dijkstras(graph, source):
    n = len(graph)
    distances = [sys.maxsize] *n 
    distances[source] = 0
    visited = [False]*n

    for _ in range(n):
        min_distance = sys.maxsize
        min_index = -1

        for i in range (n):
            if not visited[i] and distances[i]< min_distance:
                min_distance = distances[i]
                min_index = i
            
        visited[min_index] = True
        
        for i in range(n):
            if graph[min_index][i] >0 and not visited[i] and distances[i]> distances[min_index]+ graph[min_index][i]:
                distances[i] = distances[min_index]+ graph[min_index][i]
                
    return distances
        


connections = [
    [1, 2, 10],
    [1, 5, 100],
    [2, 3, 50],
    [5, 4, 60],
    [3, 4, 20],
    [5, 3, 10]
]

vertices_num = len(connections)

graph = [[0]* vertices_num for _ in range(vertices_num)]

for connection in connections:
    start, end, cost = connection
    graph[start-1][end -1] = cost
    graph[end -1][start-1] = cost

source = 0
distances = dijkstras(graph, source)

print("Distances from source ",source+1)
for i in range(vertices_num-1):
    print(f"{source+1} to {i+1} is {distances[i]}")