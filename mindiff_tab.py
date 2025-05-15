def min_difference_tabulation(arr):
    total_sum=sum(arr)
    n=len(arr)
    half_sum=total_sum//2
    dp = [[False] * (half_sum + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,half_sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    
    for j in range(half_sum, -1, -1):
        if dp[n][j]:
            return total_sum -2 *j
arr=[1,6,11,5]
print(min_difference_tabulation(arr))