class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_min = [-1 for i in range(len(heights))]
        left_stack = []

        for i in range(len(heights)):
            curr = heights[i]

            while len(left_stack) > 0 and heights[left_stack[-1]] >= curr:
                left_stack.pop()
            
            if len(left_stack) > 0:
                left_min[i] = left_stack[-1]

            left_stack.append(i)
        
        right_min = [len(heights) for i in range(len(heights))]
        right_stack = []

        for i in range(len(heights) - 1, -1, -1):
            curr = heights[i]

            while len(right_stack) > 0 and heights[right_stack[-1]] >= curr:
                right_stack.pop()
            
            if len(right_stack) > 0:
                right_min[i] = right_stack[-1]


            right_stack.append(i)

        res = 0

        for i in range(len(heights)):
            height = heights[i]

            left_extend = i - left_min[i] - 1
            right_extend = right_min[i] - i - 1
            width = 1 + left_extend + right_extend
            res = max(res, height * width)


        return res
