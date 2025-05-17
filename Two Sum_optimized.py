def twoSum(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while(low<high):
        sum=nums[low]+nums[high]
        if sum==target:
            return "Yes"
        elif sum<target:
            low+=1
        elif  sum>target:
            high-=1
        else:
            return "No"
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))
