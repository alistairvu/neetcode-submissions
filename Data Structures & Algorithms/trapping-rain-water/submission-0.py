class Solution:
    def trap(self, height: List[int]) -> int:
        right_max = [0 for _ in height]
        left_max = [0 for _ in height]

        curr_max = 0

        for idx in range(len(height) - 1, -1, -1):
            right_max[idx] = curr_max
            curr_max = max(curr_max, height[idx])

        curr_max = 0

        for idx in range(len(height)):
            left_max[idx] = curr_max
            curr_max = max(curr_max, height[idx])


        res = 0

        for i in range(len(height)):
            res += max(0, min(right_max[i], left_max[i]) - height[i])

        return res

