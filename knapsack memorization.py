def knapsack(wt,prof,W,n,memo):
    if n==0 or W==0:
        return 0
    if (n,W) in memo:
        return memo[(n,W)]
    if wt[n-1]>W:
        return knapsack(wt,prof,W,n-1,memo)
    else:
        include=(prof[n-1]+knapsack(wt,prof,W-wt[n-1],n-1,memo))
        exclude=knapsack(wt,prof,W,n-1,memo)
        memo[(n,W)]=max(include,exclude)
    return memo[(n,W)]
wt=[3,4,6,5]
prof=[5,8,3,1]
W=8
n=4
memo={}
print(knapsack(wt,prof,W,n,memo))