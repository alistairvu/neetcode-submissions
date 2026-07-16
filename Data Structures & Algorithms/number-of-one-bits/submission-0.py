class Solution:
    def hammingWeight(self, n: int) -> int:
        curr = n
        res = 0

        while curr > 0:
            res += (curr % 2)
            curr = curr // 2
        
        return res