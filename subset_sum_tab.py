def is_subset_sum_tab(arr,n,target):
    dp=[[False for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    if not dp[n][target]:   
        return []
    subset=[]
    i,j=n,target
    while i>0 and j>0:
        if dp[i][j] and dp[i-1][j]:
            subset.append(arr[i-1])
            j-=arr[i-1]
        i-=1
    return subset
arr=[2,3,7,8,10]
target=10
n=len(arr)
result=is_subset_sum_tab(arr,n,target)
print("subset with given sum exists(tabulation):",result)