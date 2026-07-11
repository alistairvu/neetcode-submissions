import math

class Solution:
    def calculateHours(self, piles: List[int], k: int) -> int:
        res = 0

        for pile in piles:
            res += math.ceil(pile / k)
        
        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = 0

        while left <= right:
            mid = (left + right) // 2
            hours = self.calculateHours(piles, mid)

            if hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res