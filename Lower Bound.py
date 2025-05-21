def lowerBound( arr, target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[10,20,35,50,50,50,55,60]
k=49
print(lowerBound(arr,k))