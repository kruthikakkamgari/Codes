class Solution(object):
    def canPartition(self, nums):
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum // 2
        dp = [False] * (targetSum + 1)
        dp[0] = True
        for num in nums:
            for currSum in range(targetSum, num - 1, -1):
                dp[currSum] = dp[currSum] or dp[currSum - num]
        return dp[targetSum]

nums = [1, 5, 11, 5]
sol = Solution()
result = sol.canPartition(nums)
print("Can partition:", result)
