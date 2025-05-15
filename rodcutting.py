def cutRodRecur(i,price):
    if i==0:
        return 0
    ans=0
    for j in range(1,i+1):
        ans=max(ans,price[j-1]+cutRodRecur(i-j,price))
    return ans
def cutRod(price):
    n=len(price)
    return cutRodRecur(n,price)
price=[1,5,8,9,10,17,17,20]
print(cutRod(price))
#memoization approach
def cutRodRecur(i,price,memo):
    if i==0:
        return 0
    if memo[i-1]!=-1:
        return memo[i-1]
    ans=0
    for j in range(1,i+1):
        ans=max(ans,price[j-1]+cutRodRecur(i-j,price,memo))
    memo[i-1]=ans
    return ans
def cutRod(price):
    n=len(price)
    memo=[-1]*n
    return cutRodRecur(n,price,memo)
price=[1,5,8,9,10,17,17,20]
print(cutRod(price))
#tabulation approach
def cutRod(price):
    n=len(price)
    dp=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]=max(dp[i],price[j-1]+dp[i-j])
    return dp[n]
price=[1,5,8,9,10,17,17,20]
print(cutRod(price))