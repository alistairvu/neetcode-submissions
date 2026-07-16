class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [x for x in range(n)]
        self.size = [1 for x in range(n)]
        self.connected = n
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def merge(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]
        self.connected -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)

        for x, y in edges:
            union_find.merge(x, y)
        
        return union_find.connected


