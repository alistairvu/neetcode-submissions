class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for x in range(n + 1):
            for y in range(2):
                if x == 0:
                    dp[x][y] = 0
                elif x == 1:
                    dp[x][y] = y * nums[0]
                elif x == n and y == 1:
                    dp[x][y] = dp[x - 1][y]
                else:
                    dp[x][y] = max(dp[x - 1][y], nums[x - 1] + dp[x - 2][y])

        return max(dp[n])