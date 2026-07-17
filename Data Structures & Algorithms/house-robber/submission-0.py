class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n+1):
            if i == 1:
                dp[i] = nums[0]
                continue
        
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        return dp[n]