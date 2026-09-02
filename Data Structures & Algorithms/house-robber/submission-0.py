class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n

        dp[0] = nums[0]

        for i in range(1, n):
            if i > 1:
                rob = nums[i] + dp[i-2]
            else:
                rob = nums[i]

            notrob = dp[i-1]

            dp[i] = max(rob, notrob)

        return dp[n-1]