def max_profit(drama_requests):
    sorted_requests = sorted(drama_requests, key=lambda x: x[2])
    
    n = len(sorted_requests)
    dp = [0] * n

    for i in range(n):
        dp[i]=sorted_requests[i][3]
        for j in range(i):
            if sorted_requests[j][2]<= sorted_requests[i][1]:
                dp[i] = max(dp[i], dp[j] + sorted_requests[i][3])

    return max(dp)

drama_requests = [
    [1, 1, 2, 100],
    [2, 2, 5, 200],
    [3, 3, 6, 300],
    [4, 4, 8, 400],
    [5, 5, 9, 500],
    [6, 6, 10, 100]
]

maximum_profit = max_profit(drama_requests)
print("Maximum Profit:", maximum_profit)
