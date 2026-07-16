class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)

        for i in range(n):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i
        
        return [-1, -1]