def is_subset_sum(arr,n,target):
    if n==0:
        return False
    if target==0:
        return True
    if arr[n-1]>target:
        return is_subset_sum(arr,n-1,target)
    return is_subset_sum(arr,n-1,target) + is_subset_sum(arr,n-1,target-arr[n-1])
arr=[2,3,7,8,10]
target=10 
n=len(arr)
result=is_subset_sum(arr,n,target)
print(result)