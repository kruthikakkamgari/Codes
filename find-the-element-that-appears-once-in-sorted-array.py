
def findOnce(arr):
    n=len(arr)
    if(n==1):
        return arr[0]
    elif arr[0]!=arr[1]:
        return arr[0]
    elif arr[n-1]!=arr[n-2]:
        return arr[n-1]
    low=1
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]):
            return arr[mid]
    #you are at left half
        elif((mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1])):
            low=mid+1
    #you are at right half
        elif((mid%2==0 and arr[mid]==arr[mid-1]) or (mid%2==1 and arr[mid]==arr[mid+1])):
            high=mid-1
arr=[1,1,2,2,3,3,4,4,5,6,6,7,7]
print(findOnce(arr))
            
        # Complete this function