class UnionSet:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.size = [1 for x in range(n)]
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]
        self.size[py] = 0

    def max_size(self):
        return max(self.size)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        union_set = UnionSet(n)
        seen = {}

        for i in range(n):
            if nums[i] in seen:
                continue
            
            if nums[i] - 1 in seen:
                union_set.union(i, seen[nums[i] - 1])
            
            if nums[i] + 1 in seen:
                union_set.union(i, seen[nums[i] + 1])
            
            seen[nums[i]] = i

        return union_set.max_size()