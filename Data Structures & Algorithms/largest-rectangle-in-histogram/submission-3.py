"""
use a monotonic stack that contains a tuple pair of index and height

while the height is smaller than the top, keep popping and keep track of the starting index

update the res and after done popping, the new height inherits the old starting position

if there is elements left in stack process them and return res

O(N), O(N)

heights = [7,1,7,2,2,4]
res = 7

[(0, 1), (2, 2), (4, 2), (5, 4)]


"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        res = 0 

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][-1]:
                start, height = stack.pop()
                res = max(res, height * (i - start))
            stack.append((start, h))

        n = len(heights)
        for i, h in stack:
            res = max(res, h * (n - i))
        return res