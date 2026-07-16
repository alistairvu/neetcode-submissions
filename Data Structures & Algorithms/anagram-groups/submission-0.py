class Solution:
    def get_freq(self, x):
        res = [0 for _ in range(26)]

        for char in x:
            idx = ord(char) - ord('a')
            res[idx] += 1

        return tuple(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        groups = {}

        for x in strs: # O(n)
            freq = self.get_freq(x) # O(m)

            if freq in groups:
                groups[freq].append(x)
            else:
                groups[freq] = [x]

        res = []

        for group in groups:
            res.append(groups[group])

        return res