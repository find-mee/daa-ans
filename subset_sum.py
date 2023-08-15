def is_subset_sum(nums, target_sum):
    n = len(nums)
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]
    print(dp)
    print()
    # A sum of 0 is always possible with an empty subset
    for i in range(n + 1):
        dp[i][0] = True
    print(dp)

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]

def display_solution(nums, target_sum):
    if is_subset_sum(nums, target_sum):
        print("A subset with the given sum exists.")
    else:
        print("No subset with the given sum exists.")

# Example usage
nums = [3, 34, 4, 12, 5, 2]
target_sum = 9

display_solution(nums, target_sum)
