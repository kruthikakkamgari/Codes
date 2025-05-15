def coinChange(coins,amount):
    dp=[amount+1]*(amount+1)
    dp[0]=0
    for i in coins:
        for j in range(i,amount+1):
            dp[j]=min(dp[j],dp[j-1]+1)
        if dp[amount]!=amount+1:
            return dp[amount]
        else:
            return -1
coins=[1,2,5]
amount=11
print(coinChange(coins,amount))