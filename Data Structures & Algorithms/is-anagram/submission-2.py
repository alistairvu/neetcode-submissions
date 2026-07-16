class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqs = [0 for _ in range(26)]

        for char in s:
            idx = ord(char) - ord('a')
            freqs[idx] += 1
        
        for char in t:
            idx = ord(char) - ord('a')

            if freqs[idx] <= 0:
                return False
            freqs[idx] -= 1

        return sum(freqs) == 0