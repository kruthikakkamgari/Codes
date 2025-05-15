def subsets(nums):
    res = []
    def backtrack(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
        backtrack(i + 1, path)
    backtrack(0, [])
    return res
nums = [1, 2, 3]
print(subsets(nums))