def searchRange(nums,target):
    def getLowerBound(nums,target):
        n=len(nums)
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>=target):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def getUpperBound(nums,target):
        n=len(nums)
        low=0
        high=n-1
        ans=n
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>target):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    lb=getLowerBound(nums,target)
    if(lb==-1 or nums[lb]!=target):
        return [-1,-1]
    ub=getUpperBound(nums,target)-1
    return [lb,ub]
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))

