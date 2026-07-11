class Solution:
    def findMinIndex(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= nums[-1]:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
    
    def binarySearch(self, nums: list[int], target: int, left_start: int, right_start: int) -> int:
        left, right = left_start, right_start

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


    def search(self, nums: List[int], target: int) -> int:
        min_index = self.findMinIndex(nums)

        if min_index == 0:
            return self.binarySearch(nums, target, 0, len(nums) - 1)
        
        if target >= nums[min_index] and target <= nums[-1]:
            return self.binarySearch(nums, target, min_index, len(nums) - 1)
        
        return self.binarySearch(nums, target, 0, min_index - 1)