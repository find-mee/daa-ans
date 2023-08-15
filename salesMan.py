def tsp_dynamic_programming(graph):
    n = len(graph)
    all_sets = 2 ** n  # Total number of subsets
    
    # Initialize the DP table (memoization table)
    dp = [[float('inf')] * n for _ in range(all_sets)]
    
    # Base case: Starting from city 0 and ending at city 0 with no other cities visited
    dp[1][0] = 0
    
    for mask in range(1, all_sets):
        for u in range(n):
            if mask & (1 << u):  # If city u is in the current subset
                for v in range(n):
                    if v != u and mask & (1 << v):  # If city v is also in the subset
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u])
    
    # Find the optimal tour length by considering all cities as the last stop
    optimal_tour = float('inf')
    for u in range(1, n):
        optimal_tour = min(optimal_tour, dp[all_sets - 1][u] + graph[u][0])
    
    return optimal_tour

# Example usage
graph = [
    [0, 2, float('inf'), 12, 5],
    [2, 0, 4, 8, float('inf')],
    [float('inf'), 4, 0, 3, 3],
    [12, 8, 3, 0, 10],
    [5, float('inf'), 3, 10, 0]
    
]

optimal_tour = tsp_dynamic_programming(graph)
print("Optimal Tour Length:", optimal_tour)
