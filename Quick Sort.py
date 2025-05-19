def quickSort(arr):
    def qs(arr,low,high):
        if low<high:
            pIndex=partition(arr,low,high)
            qs(arr,low,pIndex-1)
            qs(arr,pIndex+1,high)
    def partition(arr,low,high):
        i=low
        j=high
        pivot=arr[low]
        while(i<j):
            while(arr[i]<=pivot and i<high):
                i+=1
            while(arr[j]>=pivot and j>low):
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
    n=len(arr)
    low=0
    high=n-1
    qs(arr,low,high)
    return arr
arr=[1,8,9,5,7,2,3]
print(quickSort(arr))
    

            