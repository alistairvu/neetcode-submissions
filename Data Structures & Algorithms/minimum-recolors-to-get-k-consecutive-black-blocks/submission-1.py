class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0

        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
            
        res = white_count
        n = len(blocks)

        for i in range(k, n):
            last_idx = i - k

            if blocks[last_idx] == 'W':
                white_count -= 1
            
            if blocks[i] == 'W':
                white_count += 1
            
            res = min(res, white_count)
        
        return res