
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        for x in range(n + 1):
            for y in range(amount + 1):
                if y == 0:
                    dp[x][y] = 0
                elif x == 0:
                    dp[x][y] = float("inf")
                elif y < coins[x - 1]:
                    dp[x][y] = dp[x - 1][y]
                else:
                    dp[x][y] = min(dp[x - 1][y], 1 + dp[x][y - coins[x - 1]])

        return dp[n][amount] if dp[n][amount] != float("inf") else -1