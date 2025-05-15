def find_min_difference(arr,n,sum_cal,sum_total,memo):
    if n==0:
        return abs((sum_total-sum_cal)-sum_cal)
    if (n,sum_cal) in memo:
        return memo[(n,sum_cal)]
    include=find_min_difference(arr,n-1,sum_cal+arr[n-1],sum_total,memo)
    exclude=find_min_difference(arr,n-1,sum_cal,sum_total,memo) 
    memo[(n,sum_cal)]=min(include,exclude)
    return memo[(n,sum_cal)]
def min_difference(arr):
    sum_total=sum(arr)
    memo={}
    return find_min_difference(arr,len(arr),0,sum_total,memo)
arr=[1,6,11,5]
print(min_difference(arr))