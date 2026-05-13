"""
Create a stack to store tuples of an index and its height
While the curr height is less than the top of the stack
    continously pop from the stack and calculate the area 
    keep track of the last index we popped since we'll be using it to append to the stack 
    (this is because the current height can extend left so we want to start where we stopped popping)

While there's still tuples in the stack, keep processing until it's empty
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (i-index) * height)
                start = index
            stack.append((start,h))

        n = len(heights)
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, (n-index) * height)

        return max_area
