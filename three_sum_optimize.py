class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for  i in range(0,n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=n-1
            while(j<k):
                Sum=nums[i]+nums[j]+nums[k]
                if (Sum<0):
                    j+=1
                elif Sum>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j-1]==nums[j]:
                        j+=1
                    while j<k and nums[k+1]==nums[k]:
                        k-=1
        return ans


