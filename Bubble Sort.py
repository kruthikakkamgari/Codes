def BubbleSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[13,46,98,9,56]
print(BubbleSort(arr))
