def fun(nums):
    def rec(nums, i):
        if i == len(nums)-1:
            return nums[i], nums[i]
        min,max=rec(nums,i+1)      
        min= min if min<nums[i] else nums[i]
        max= max if max>nums[i] else nums[i]
        return min,max
    return rec(nums,0)
min,max=fun([5,3,7,9,2])
print(min,max)