import heapq

class Union:
    def __init__(self, n: int):
        self.n = n
        self.parents = [x for x in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, x: int):
        if self.parents[x] == x:
            return x
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)
    
    def merge(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]

        if self.size[px] == self.n:
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph_union = Union(n)
        edges = []

        for i in range(1, n):
            for j in range(0, i):
                i_x, i_y = points[i]
                j_x, j_y = points[j]
                distance = abs(i_x - j_x) + abs(i_y - j_y)
                edges.append((distance, i, j))
        
        heapq.heapify(edges)
        res = 0

        while edges:
            c, x, y = heapq.heappop(edges)

            if graph_union.same(x, y):
                continue
            
            res += c

            if graph_union.merge(x, y):
                return res
        
        return res

        