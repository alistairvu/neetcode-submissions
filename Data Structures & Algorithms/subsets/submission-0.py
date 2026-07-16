class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            if idx == len(nums):
                res.append(list(path))
                return
            
            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()

            dfs(idx + 1, path)
        
        dfs(0, [])
        return res