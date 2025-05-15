def knapsack_tabulation(wt,prof,W,n):
    dp=[[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1]<=w:
                dp[i][w]=max(prof[i-1]+dp[i-1][W-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]
wt=[3,4,6,5]
prof=[2,3,1,4]
W=8
n=4
print("output(Tabulation):",knapsack_tabulation(wt,prof,W,n))