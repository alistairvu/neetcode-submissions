class Solution:
    def hammingWeight(self, n: int) -> int:
        curr = n
        res = 0

        while curr > 0:
            res += (curr & 1)
            curr = curr >> 1
        
        return res