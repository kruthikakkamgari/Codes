def fun(nums):
    def rec(nums,i):
        if i==len(nums)-1:
            return nums[i]
        min=rec(nums,i+1)
        return min if min<nums[i] else nums[i]

    return rec(nums,0)
print(fun([5,3,7,9,2]))
