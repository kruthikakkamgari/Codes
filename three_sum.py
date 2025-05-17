def triplet_sum(nums):
    triplet_sum=set()
    n=len(nums)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(nums[i]+nums[j]+nums[k]==0):
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    triplet_sum.add(tuple(temp))
    ans=[]
    for triplet in triplet_sum:
        ans.append(list(triplet))
    return ans
nums=[1,2,0,-1,3]
print(triplet_sum(nums))

