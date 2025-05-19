def selection(arr,n):
    for i in range(0,n):
        Min=i
        for j in range(i+1,n):
            if(arr[j]<arr[Min]):
                Min=j
        arr[i],arr[Min]=arr[Min],arr[i]
    return arr
arr=[1,8,9,5,7,2,3]
n=len(arr)
print(selection(arr,n))