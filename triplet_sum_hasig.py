def triplet_sum(nums,):
    triplet_sum=set()
    n=len(nums)
    for i  in range(0,n-1):
        hashmap=[]
        for j in range(i+1,n):
            k=-(nums[i]+nums[j])
            if  k in hashmap:
                temp=[nums[i],nums[j],k]
                temp.sort()
                triplet_sum.add(tuple(temp))
            hashmap.append(nums[j])
    ans=[]
    for triplet in triplet_sum:
        ans.append(list(triplet))
    return ans
nums=[1,2,0,-1,3]
print(triplet_sum(nums))