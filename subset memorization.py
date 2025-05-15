def is_subset_sum_memo(arr,n,target,dp):
    if n==0:
        return False
    if target==0:
        return True
    if dp[n][target]!=1:
        return dp[n][target]
    if arr[n-1]>target:
        dp[n][target]=is_subset_sum_memo(arr,n-1,target,dp)
    else:
        include=is_subset_sum_memo(arr,n-1,target-arr[n-1],dp)
        exclude=is_subset_sum_memo(arr,n-1,target,dp)
        dp[n][target]=include or exclude
    return dp[n][target]
arr=[3,34,4,12,5,2]
target=9
n=len(arr)
dp=[[-1 for _ in range(target+1)] for _ in range(n+1)]
result=is_subset_sum_memo(arr,n,target,dp)
print("subset with given sum exists(memo):",result)