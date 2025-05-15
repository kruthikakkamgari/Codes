def knapsack(wt,prof,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return knapsack(wt,prof,W,n-1)
    else:
        include=(prof[n-1]+knapsack(wt,prof,W-wt[n-1],n-1))
        exclude=knapsack(wt,prof,W,n-1)
        return max(include,exclude)
wt=[3,4,6,5]
prof=[5,8,3,1]
W=8
n=4
print(knapsack(wt,prof,W,n))