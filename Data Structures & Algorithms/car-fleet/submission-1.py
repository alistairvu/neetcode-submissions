class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = [(pos, s) for pos, s in zip(position, speed)]
        tuples.sort(key=lambda x: (-x[0], -x[1]))

        stack = []

        for pos, s in tuples:
            if len(stack) > 0:
                last_pos, last_s = stack[-1]
                last_time = (target - last_pos) / last_s
                this_time = (target - pos) / s

                if this_time <= last_time:
                    continue
            
            stack.append((pos, s))



        return len(stack)