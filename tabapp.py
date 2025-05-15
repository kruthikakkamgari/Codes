def lcs_dp(x,y):
    m,n=len(x),len(y)
    dp=[[0]*(n+1)for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[i-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]  
x="agbcdf"
y="abcalmng"
print(lcs_dp(x,y))