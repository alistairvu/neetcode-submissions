

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums_set = set(nums)

        for val in nums:
            if val - 1 in nums_set:
                continue
            
            length = 1

            while val + length in nums_set:
                length += 1
            
            res = max(res, length)


        return res