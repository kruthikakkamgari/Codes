class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for a in range(0,n):
            b=target-nums[a]
            if b in d:
                return [a,d[b]]
            else:
                d[nums[a]]=a
        
        