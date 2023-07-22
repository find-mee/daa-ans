def dfs(graph,visited,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(graph,visited,neighbour)

graph = {
    '0':['3','1'],
    '1':['0','2','4'],
    '2':['0','1','4'],
    '3':['0','4'],
    '4':['2','1','3']
}

visited = set()
root = '0'
dfs(graph,visited,root)