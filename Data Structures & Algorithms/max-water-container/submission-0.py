class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        answer = 0

        while left <= right:
            answer = max(
                answer,
                min(heights[left], heights[right]) * (right - left)
            )

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return answer