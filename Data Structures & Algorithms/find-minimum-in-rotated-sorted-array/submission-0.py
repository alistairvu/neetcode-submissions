class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1 
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= nums[-1]:
                ans = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return ans