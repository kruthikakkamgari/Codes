def subsets(nums):
    result = []
    nums.sort()
    def backtrack(start=0, path=[]):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack()
    return result
nums = [1, 2, 2]
print(subsets(nums))