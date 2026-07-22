class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        res = ""

        for diff in range(n + 1):
            for i in range(0, n + 1 - diff):
                j = i + diff

                if diff <= 1:
                    dp[i][j] = True
                    res = s[i:j]
                else:
                    dp[i][j] = (s[i] == s[j - 1]) and dp[i + 1][j - 1]
                    
                    if dp[i][j] and diff > len(res):
                        res = s[i:j]
        
        return res