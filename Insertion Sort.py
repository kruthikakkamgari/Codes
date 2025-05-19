def insertionSort( arr):
    n=len(arr)
    for i in range(0,n):
        while(i>0 and arr[i-1]>arr[i]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    return arr
arr=[23,56,10,2,9]
print(insertionSort(arr))

