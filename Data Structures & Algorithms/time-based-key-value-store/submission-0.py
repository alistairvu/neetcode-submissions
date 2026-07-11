class TimeMap:

    def __init__(self):
        self.values = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        
        vals = self.values[key]
        left, right = 0, len(vals) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            curr_val, curr_time = vals[mid]

            if curr_time <= timestamp:
                res = curr_val
                left = mid + 1
            else:
                right = mid - 1
        
        return res
