def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        k=partition(arr,low,high)
        quick_sort(arr,low,k-1)
        quick_sort(arr,k+1,high)


arr=list(map(int,input().split()))
n=len(arr)
quick_sort(arr, 0, n - 1)

print("Soretd array: ",arr)
