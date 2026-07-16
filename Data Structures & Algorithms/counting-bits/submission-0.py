class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]
        next_pow = 1

        for i in range(1, n + 1):
            if i == next_pow:
                next_pow *= 2
                res[i] = 1
                continue
            
            prev_pow = next_pow // 2
            res[i] = res[prev_pow] + res[i - prev_pow]

        return res
