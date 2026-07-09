class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for t in temperatures]
        stack = []
        
        for i in range(len(temperatures)):
            current = temperatures[i]

            while len(stack) > 0:
                stack_tail = stack[-1]

                if temperatures[stack_tail] < current:
                    stack.pop()
                    res[stack_tail] = i - stack_tail
                else:
                    break
            
            stack.append(i)
        
        return res