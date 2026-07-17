class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        res = 0

        for diff in range(n + 1):
            for i in range(0, n + 1 - diff):
                j = i + diff

                if diff <= 1:
                    dp[i][j] = True
                    
                    if diff == 1:
                        res += 1
                else:
                    dp[i][j] = (s[i] == s[j - 1]) and dp[i + 1][j - 1]
                    
                    if dp[i][j]:
                        res += 1
        
        return res