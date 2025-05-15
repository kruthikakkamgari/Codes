def min_difference (arr,n,sumcal,sum_total):
    if n==0:
        return abs((sum_total-sumcal)-sumcal)
    include=min_difference(arr,n-1,sumcal+arr[n-1],sum_total)
    exclude=min_difference(arr,n-1,sumcal,sum_total)
    return min(include,exclude)
def min_diff(arr):
    sum_total=0
    for num in arr:
        sum_total+=num
    return min_difference(arr,len(arr),0,sum_total)
arr=[1,6,11,5]
print(min_diff(arr))