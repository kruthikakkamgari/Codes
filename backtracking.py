def permute(path,nums,results):
    if len(path)==len(nums):
        results.append(path[:])
        return
    for num in nums:
        if num not in path:
            permute(path+[num],nums,results)
nums=[1,2,3]
results=[]
permute([],nums,results)
print("All permutation:")
for r in results:
  print(r)