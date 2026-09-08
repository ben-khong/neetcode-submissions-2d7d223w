"""
[30,38,30,36,35,40,28]

stack = [[0,30]]
res = [0, 0, 0, 0, 0, 0, 0]
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][-1] < t:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append((i, t))
        
        return res


    