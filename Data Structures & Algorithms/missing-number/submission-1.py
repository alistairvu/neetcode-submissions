class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for num in nums:
            num_abs = abs(num) if num != -(n + 1) else 0

            if num_abs < n:
                nums[num_abs] = -1 * abs(nums[num_abs]) if nums[num_abs] != 0 else -(n + 1)
        

        for i in range(n):
            if nums[i] >= 0:
                return i
        
        return n